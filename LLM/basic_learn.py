import os
import openai
from openai import OpenAI
from transformers import AutoTokenizer , AutoModelForCausalLM
from transformers import AutoModelForSeq2SeqLM
import torch
import torch.nn as nn
import re

API_KEY = "sk-SD3QkuWcKeF8cLAjZel0kn2scMyycuOQFiuVyTRsPNOuy1FP"
BASE_URL = "https://api.chatanywhere.tech/v1"



# def promptGenerator(fewshot_content , function_to_test):
#     fewshot_prompt = f"""I have a Python method defined as follows
#     {function_to_test}
#     {fewshot_content}
#
#
#
#     #</code>
#
#     #<test>
#
#     def test():
#         assert
#     """
#     return fewshot_prompt


def promptGenerator(fewshot_content, function_to_test):
    fewshot_prompt = f"""Here are some example unit test cases for methods:
    {fewshot_content}

I have a Python method defined as follows:
    {function_to_test}
Please generate 3 to 7 unit test cases for this method like examples mentioned above. The tests should:
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


def get_completion(prompt, model="gpt-3.5-turbo",
                   reruns_if_empty: int = 2,
                   reruns_no_assert: int = 2):
    client = OpenAI(api_key=API_KEY,
                    base_url=BASE_URL)
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.8,
        max_tokens=500,
    )
    print(response.choices[0].message.content)
    print(response.choices[0].logprobs.content)
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
    # if reruns_no_assert > 0 and re.search('assert', explanation_completion):
    #     print("no assert in output")
    # else:
    #     print(explanation_completion)
    #
    # return explanation_completion

# print(get_completion("Please introduce Nanjing University"))

def get_data(DATA_SET):
    CODE_DIR = os.path.join(os.getcwd() , DATA_SET)
    # print(CODE_DIR)
    entries = os.listdir(CODE_DIR)
    file_count = sum(1 for entry in entries if os.path.isfile(os.path.join(CODE_DIR , entry)))
    # print(file_count)
    return CODE_DIR , file_count

def get_fewshot():
    fewshot_path = os.path.join(os.getcwd() , "few_shot_query.py")
    with open(fewshot_path , encoding='utf-8') as fewshot:
        fewshot_content = fewshot.read()
    return fewshot_content.lstrip()

#whether to use fewshot or not
def call_LLM(DATA_SET , fewshot):
    CODE_DIR , file_count = get_data(DATA_SET)
    for i in range(2):
        file_name = str(i) + ".py"
        CODE_PATH = os.path.join(CODE_DIR , file_name)
        # print(CODE_PATH)
        with open(CODE_PATH , encoding='utf-8') as input_code:
            function_to_test = input_code.read()

        function_to_test = function_to_test.split("METADATA")
        print(i)
        # print(function_to_test)

        if(fewshot == "fewshot"):
            fewshot_content = get_fewshot()
            init_prompt = promptGenerator(fewshot_content, function_to_test)
            # print(init_prompt)
            print(get_completion(init_prompt))
            print("###################################################")




call_LLM("HumanEval" , "fewshot")
# print(get_completion(init_prompt))