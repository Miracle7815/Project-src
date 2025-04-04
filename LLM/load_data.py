import os
import re

import openai
from openai import OpenAI

API_KEY = "sk-SD3QkuWcKeF8cLAjZel0kn2scMyycuOQFiuVyTRsPNOuy1FP"
BASE_URL = "https://api.chatanywhere.tech/v1"

def get_data(DATA_SET):
    CODE_DIR = os.path.join(os.getcwd() , DATA_SET)
    # print(CODE_DIR)
    entries = os.listdir(CODE_DIR)
    file_count = sum(1 for entry in entries if os.path.isfile(os.path.join(CODE_DIR , entry)))
    # print(file_count)

    for i in range(file_count):
        file_name = str(i) + ".py"
        CODE_PATH = os.path.join(CODE_DIR , file_name)
        # print(CODE_PATH)
        with open(CODE_PATH , encoding='utf-8') as input_code:
            function_to_test = input_code.read()

        function_to_test = function_to_test.split("def check")[0].lstrip()
        # print(i)
        # print(function_to_test)

def get_fewshot():
    fewshot_path = os.path.join(os.getcwd() , "few_shot_query.py")
    with open(fewshot_path , encoding='utf-8') as fewshot:
        fewshot_content = fewshot.read()
    return fewshot_content.lstrip()


def get_completion(prompt, model="gpt-3.5-turbo" ,
                   reruns_if_empty: int = 2,
                   reruns_no_assert: int = 2):
    client = OpenAI(api_key=API_KEY,
                    base_url=BASE_URL)
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
        max_tokens=300
    )

    print(response.choices[0].message.content)
    # explanation_completion = response.choices[0].message.content
    #
    # if reruns_if_empty > 0 and all(elem == '\n' for elem in explanation_completion):
    #     print("empty output")
    #     # return get_completion(prompt , model = model ,
    #     #                       reruns_if_empty= reruns_if_empty - 1,
    #     #                       reruns_no_assert = reruns_no_assert)
    # else:
    #     print(explanation_completion)
    #
    # if reruns_no_assert > 0 and re.search('assert' , explanation_completion):
    #     print("no assert in output")
    #
    # return explanation_completion


def promptGenerator(fewshot_content , function_to_test):
    fewshot_prompt = f"""Here are some example unit test cases for methods:
    {fewshot_content}
    
I have a Python method defined as follows:
    {function_to_test}
Please generate unit test cases for this method like examples mentioned above. The tests should:
1. Cover different edge cases and input scenarios.
2. Verify the correctness of the method's output.
3. Handle cases where invalid input might occur.

For each test case, please provide:
- A short explanation of what the test is verifying.
- The corresponding code for the test.
"""
    return fewshot_prompt

def fewshotGenerator(fewshot_query):
    fewshot = fewshot_query.split("#<code>")
    fewshot_content = fewshot[0]
    for i in range(1 , len(fewshot)):
        fewshot_content += f"Example {i}\nMethod:\n#<code>"
        fewshot_content += fewshot[i].split("#<test>")[0]
        fewshot_content += "\nTest cases:\n#<test>"
        fewshot_content += fewshot[i].split("#<test>")[1] + "\n"
    # print(fewshot_content)
    return fewshot_content


fewshot_content = """
#<code>
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
#</code>
#<test>
def test_equilateral_triangle():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>
#<code>
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>
#<test>
def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>
"""

function_to_test = '''
    from typing import List
    
    def below_zero(operations: List[int]) -> bool:
        """ You're given a list of deposit and withdrawal operations on a bank account that starts with
        zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
        at that point function should return True. Otherwise it should return False.
        >>> below_zero([1, 2, 3])
        False
        >>> below_zero([1, 2, -4, 5])
        True
        """
        balance = 0
    
        for op in operations:
            balance += op
            if balance < 0:
                return True
    
        return False
'''


prompt = promptGenerator(fewshotGenerator(fewshot_content) , function_to_test)
get_completion(prompt)
# get_completion("Please introduce NanJing university")
# get_data("HumanEval")
# print(get_fewshot())