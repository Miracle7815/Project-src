import os
import re

from langchain.prompts import FewShotChatMessagePromptTemplate , ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import LLMResult

from LISP.function_file import write_result_for_humaneval
from function_file import create_prompt_for_input_generation , create_prompt_for_input_generation_few_shot , write_result

# 控制台
# API_KEY = "sk-SD3QkuWcKeF8cLAjZel0kn2scMyycuOQFiuVyTRsPNOuy1FP"
# BASE_URL = "https://api.chatanywhere.tech/v1"


# 控制台
API_KEY = "sk-YXeIf5Hzq452SluTP77QPGWOeWHq7GFMqH4C4kwr9uFZhbhv"
BASE_URL = "https://api.openai-proxy.org/v1"

#deep seek
# API_KEY = "sk-a89d7bc99b7344a7826c0291520de73c"
# BASE_URL = "https://api.deepseek.com"

SPECIFICATION_DIR = os.path.join(os.getcwd() , "HumanEval_result" , "equivalence_result")
CODE_DIR = os.path.join(os.getcwd() , "HumanEval")

class InputGeneration:
    def __init__(self , llm , prompt):
        self.llm = llm
        self.prompt = prompt

    def parse_result_1(self , result: LLMResult , document_name , file_name):
        text = result.generations[0][0].text
        write_result_for_humaneval(document_name , file_name , text)

    def run(self , code , spec , document_name , file_name):
        messages = self.prompt.format_messages(code=code , spec=spec)
        for message in messages:
            print(f"\33[32m{message.content}\033[0m\n")
        llm_result: LLMResult = self.llm.generate([messages])
        self.parse_result_1(llm_result , document_name , file_name)

SYSTEM_MESSAGE = """
You are an experienced tester. Now you are expected to write test inputs for the provided method in the Junit format.
Your answer must contain two part, the code to instantiate the objects and the required import statements.
"""

QUESTION_MESSAGE = [
    ("human",
     "API Method: ```java {code}```\n\nInput Specification: {spec}\n\n\n"),
    ("ai", "Anwser: Let's do this step by step. "),
]

EXAMPLE_MESSAGE = [
    ("human",
     "API Method: ```java {code}```\n\nInput Specification: {spec}\n\n\n"),
    ("ai", "Anwser: Let's do this step by step. {answer}"),
]

EXAMPLES = [
    {
        "code": """
    int countMatches(final CharSequence str, final char ch) {
        if (isEmpty(str)) {
            return 0;
        }
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (ch == str.charAt(i)) {
                count++;
            }
        }
        return count;
    }
    """, "spec": """
    1. `str`: is a sentence without same characters; 2. `ch`: is a character which is a part of `str`
    """, "answer": """
According to the signature of the code, we can know that we should write instances of `str` and `sh`.
In the input specification, `str` cannot have the same characters. "afghjqwryir" indicates a sentence without same characters. 
Based on the method signature, body, we can write instances of `str` and `ch` and required import statements based on and the input specification:

Example 1: 
    ```java
    import java.lang.String;
    
    public class TEST_countMatches {
        @Test(timeout = 4000)
        public void test_0() throws java.lang.Exception {
            String str = new String("afghjqwryi");
            char ch = 'j';
            int result = countMatches(str , ch);
            org.junit.Assert.assertEquals(result , 1);
        }
    }
    ```
    """}, {
        "code": """
    void bubbleSort(int[] array) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                if (array[j] > array[j + 1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    """, "spec": """
    1. `array`: is an unsorted array;
    """, "answer": """
According to the signature of the code, we can know that we should write instances of `array`.
In the input specification, `array` is an unsorted array with some integers.
Based on the method signature, body, we can write instances of `array` and required import statements based on and the input specification:

Example 1: 
        ```java
        import java.lang.Integer;
        public class TEST_bubbleSort {
            @Test(timeout = 4000)
            public class Test_0() throws java.lang.Exception {
                int[] array = {5, 6, 1, 9, 7};
                bubbleSort(array);
                org.junit.Assert.assertEquals(array , {1 , 5 , 6 , 7 , 9});
            }
        }
        ```

Example 2:
        ```java
        import java.lang.Integer;
        public class TEST_bubbleSort {
            @Test(timeout = 4000)
            public class Test_1() throws java.lang.Exception {
                int[] array = {2, 6, 3, 1, 8};
                bubbleSort(array);
                org.junit.Assert.assertEquals(array , {1 , 2 , 3 , 6 , 8});
            }
        }
        ```
    """}
]

# EXAMPLES = [
#     {
#         "code": """
#     int countMatches(final CharSequence str, final char ch) {
#         if (isEmpty(str)) {
#             return 0;
#         }
#         int count = 0;
#         for (int i = 0; i < str.length(); i++) {
#             if (ch == str.charAt(i)) {
#                 count++;
#             }
#         }
#         return count;
#     }
#     """, "spec": """
#     1. `str`: is a sentence without same characters; 2. `ch`: is a character which is a part of `str`
#     """, "answer": """
# According to the signature of the code, we can know that we should write instances of `str` and `sh`.
# In the input specification, `str` cannot have the same characters. "afghjqwryir" indicates a sentence without same characters.
# Based on the method signature, body, we can write instances of `str` and `ch` and required import statements based on and the input specification:
#
# Example 1:
#     Part 1. The objects initialized:
#         ```java
#         String str = new String("afghjqwryi");
#         char ch = 'j';
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.String;
#         ```
#
# Example 2:
#     Part 1. The objects initialized:
#         ```java
#         String str = new String("zsxdhljqwr");
#         char ch = 's';
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.String;
#         ```
#     """}, {
#         "code": """
#     <E> List<E> union(final List<? extends E> list1, final List<? extends E> list2) {
#         final ArrayList<E> result = new ArrayList<>(list1.size() + list2.size());
#         result.addAll(list1);
#         result.addAll(list2);
#         return result;
#     }
#     """, "spec": """
#     1. `list1`: is an ArrayList; 2. `list2`: is a LinkedList and the type of elements is same as `list1`'s elements' type
#     """, "answer": """
# According to the signature of the code, we can know that we should write instances of `list1` and `list2`.
# In the input specification, `list1` and `list2` have the same type of elements. ArrayList and LinkedList are both implementations of List.
# Based on the method signature, body, we can write instances of `list1` and `list2` and required import statements based on and the input specification:
#
# Example 1:
#     Part 1. The objects initialized:
#         ```java
#         List<String> list1 = new ArrayList<>();
#         List<String> list2 = new LinkedList<>();
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.String;
#         import java.util.List;
#         import java.util.ArrayList;
#         import java.util.LinkedList;
#         ```
#
# Example 2:
#     Part 1. The objects initialized:
#         ```java
#         List<Integer> list1 = new ArrayList<>();
#         List<Integer> list2 = new LinkedList<>();
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.Integer;
#         import java.util.List;
#         import java.util.ArrayList;
#         import java.util.LinkedList;
#         ```
#     """}, {
#         "code": """
#     int nextInt(final int startInclusive, final int endExclusive) {
#         Validate.isTrue(endExclusive >= startInclusive,
#                 "Start value must be smaller or equal to end value.");
#         Validate.isTrue(startInclusive >= 0, "Both range values must be non-negative.");
#
#         if (startInclusive == endExclusive) {
#             return startInclusive;
#         }
#
#         return startInclusive + random().nextInt(endExclusive - startInclusive);
#     }
#     """, "spec": """
#     1. `startInclusive`: is positive; 2. `endExclusive`: is greater than `startInclusive`
#     """, "answer": """
# According to the signature of the code, we can know that we should write instances of `startInclusive` and `endExclusive`.
# In the input specification, `startInclusive` is a positive integer. "endExclusive" should be greater than `startInclusive`.
# Based on the method signature, body, we can write instances of `startInclusive` and `endExclusive` and required import statements based on and the input specification:
#
# Example 1:
#     Part 1. The objects initialized:
#         ```java
#         int startInclusive = 2;
#         int endExclusive = 3;
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.Integer;
#         ```
#
# Example 2:
#     Part 1. The objects initialized:
#         ```java
#         int startInclusive = 1;
#         int endExclusive = 5;
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.Integer;
#         ```
#     """}, {
#         "code": """
#     void bubbleSort(int[] array) {
#         for (int i = 0; i < arr.length - 1; i++) {
#             for (int j = 0; j < arr.length - i - 1; j++) {
#                 if (array[j] > array[j + 1]){
#                     int temp = arr[j];
#                     arr[j] = arr[j + 1];
#                     arr[j + 1] = temp;
#                 }
#             }
#         }
#     }
#     """, "spec": """
#     1. `array`: is an unsorted array;
#     """, "answer": """
# According to the signature of the code, we can know that we should write instances of `array`.
# In the input specification, `array` is an unsorted array with some integers.
# Based on the method signature, body, we can write instances of `array` and required import statements based on and the input specification:
#
# Example 1:
#     Part 1. The objects initialized:
#         ```java
#         int[] array = {5, 6, 1, 9, 7};
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.Integer;
#         ```
#
# Example 2:
#     Part 1. The objects initialized:
#         ```java
#         int[] array = {2, 6, 3, 1, 8};
#         ```
#
#     Part 2. According to the code above, the following import statement must be required:
#         ```java
#         import java.lang.Integer;
#         ```
#     """}
# ]

if __name__ == "__main__":
    fewshot_prompt = create_prompt_for_input_generation_few_shot(EXAMPLE_MESSAGE , EXAMPLES)
    final_prompt = create_prompt_for_input_generation(SYSTEM_MESSAGE , fewshot_prompt , QUESTION_MESSAGE)
    # llm = ChatOpenAI(model='deepseek-chat' , openai_api_key=API_KEY , openai_api_base=BASE_URL , max_tokens=1000 , temperature=0.0)
    llm = ChatOpenAI(model='gpt-3.5-turbo', openai_api_key=API_KEY, openai_api_base=BASE_URL, max_tokens=1000, temperature=0.0)


    # if not os.path.exists(os.path.join(os.getcwd() , "gpt-result" , document_name)):
    #     os.mkdir(os.path.join(os.getcwd(), "gpt-result", document_name))

    # if not os.path.exists(os.path.join(os.getcwd(), "deepseek_result", document_name)):
    #     os.mkdir(os.path.join(os.getcwd(), "deepseek_result", document_name))


    file_name = "input_for_"
    inputGeneration = InputGeneration(llm, final_prompt)

    for root, dir, files in os.walk(SPECIFICATION_DIR):
        for file in files:
            file_name += file.split('.')[0]
            document_name = os.path.join("input_generation" , file.split('.')[0] + "_result")
            if os.path.isdir(os.path.join(os.getcwd() , "Humaneval_result" , "input_generation" , file.split('.')[0] + "_result")):
                continue
            specification = []
            EQUIVALENCE_FILE = os.path.join(SPECIFICATION_DIR , file)
            with open(EQUIVALENCE_FILE, 'r', encoding="utf-8") as class_file:
                file_content = class_file.readlines()
            # pattern_1 = r"^d+\.\s\*\*Class:\*\*"
            # pattern_2 = r"\s*- \*\*Subclasses:\*\*"
            # pattern_3 = r"\s*- \*\*Subclass.*"
            pattern = r"    1\."
            for line in file_content:
                if re.match(pattern, line):
                    specification.append(line.strip(' ').rstrip('\n'))
            print(specification)
            CODE_FILE = os.path.join(CODE_DIR , file)
            with open(CODE_FILE , 'r' , encoding="utf-8") as code_file:
                code = code_file.read()
                code_file.close()
            os.mkdir(os.path.join(os.getcwd() , "Humaneval_result" , "input_generation" , file.split('.')[0] + "_result"))
            index = 0
            for spec in specification:
                index += 1
                inputGeneration.run(code, spec, document_name, str(index))





    # with open(EQUIVALENCE_FILE , 'r' , encoding="utf-8") as file:
    #     file_content = file.readlines()
    # pattern = r"^    1\."
    # for line in file_content:
    #     if re.match(pattern , line):
    #         specification.append(line.strip(' ').rstrip('\n'))
    # print(specification)

    # while i < len(file_content):
    #     if re.match(pattern_1 , file_content[i]):
    #         sentence = ""
    #         i += 1
    #         while i < len(file_content) and not re.match(pattern_1 , file_content[i]) and not re.match(pattern_2 , file_content[i]):
    #             sentence += file_content[i].strip(' ').lstrip('- ')
    #             i += 1
    #         if i < len(file_content) and re.match(pattern_2 , file_content[i]):
    #             i += 2
    #             while i < len(file_content) and not re.match(pattern_3 , file_content[i]):
    #                 sentence += file_content[i].strip(' ').lstrip('- ')



