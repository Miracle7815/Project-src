from langchain.prompts import FewShotChatMessagePromptTemplate , ChatPromptTemplate
from langchain.schema import LLMResult
import os
from langchain.chat_models import ChatOpenAI

from LISP.function_file import write_result_for_humaneval
from function_file import write_result , create_prompt_for_partition , create_prompt_for_partition_few_shot

# 控制台
# API_KEY = "sk-SD3QkuWcKeF8cLAjZel0kn2scMyycuOQFiuVyTRsPNOuy1FP"
# BASE_URL = "https://api.chatanywhere.tech/v1"

# 免费apikey
# API_KEY = "sk-YXeIf5Hzq452SluTP77QPGWOeWHq7GFMqH4C4kwr9uFZhbhv"
# BASE_URL = "https://api.openai-proxy.org/v1"

# deep seek
# API_KEY = "sk-a89d7bc99b7344a7826c0291520de73c"
# BASE_URL = "https://api.deepseek.com"

# Qwen
# API_KEY = "sk-3d786e7826bf4ffdbe0e9d73e07c8619"
# BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# siliconflow
# API_KEY = "sk-vbraavnwvagkmnhrshcelqaytpinotzfssrwupvkdtsnfptc"
# BASE_URL = "https://api.siliconflow.cn/v1"

CODE_DIR = os.path.join(os.getcwd() , "HumanEval")

class EquivalencePartitioning:
    def __init__(self , llm , prompt):
        self.llm = llm
        self.prompt = prompt

    def parse_result(self , result: LLMResult , document_name , file_name):
        # print(type(result))
        text = result.generations[0][0].text
        write_result_for_humaneval(document_name , file_name , text)

    def run(self , code , document_name , file_name):
        messages = self.prompt.format_messages(code=code)
        for message in messages:
            print(f"\33[32m{message.content}\033[0m\n")
        llm_result: LLMResult = self.llm.generate([messages])
        self.parse_result(llm_result , document_name , file_name)


SYSTEM_MESSAGE = '''
You are an experienced tester. Now you are expected to partition the equivalence classes of the test inputs for the provided method.
In each class, your answer should start with "- class:" and specify the form of each parameter.
'''

QUESTION_MESSAGE = [
    ("human", "API Method: ```java\n {code}```"),
    ("ai", "Anwser: Let's do this step by step. "),
]

EXAMPLE_MESSAGE = [
    ("human", "API Method: ```java {code}```"),
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
    """,
        "answer": """
    Based on the method signature and body, the instances of `str` and `ch` should be generated to test the API method, 
    which represents an operation to count the number of character occurrences.
    To achieve high code coverage, diverse instances should be generated to reach different branches in the Method Body.
    Therefore, we can partition the following equivalence classes for `str` and `ch`:
    - class:
        1. `str`: is null; 2. `ch`: can be any character
    - class:
        1. `str`: is an empty string; 2. `ch`: can be any character
    - class:
        1. `str`: is a sentence without same characters; 2. `ch`: is a character which is a part of `str`
    - class:
        1. `str`: is a sentence without same characters; 2. `ch`: is a character which is not a part of `str`
    - class:
        1. `str`: is a sentence with same characters; 2. `ch`: is a character which is a part of `str`
    - class:
        1. `str`: is a sentence with same characters; `ch`: is a character which is not a part of `str`
    """
    }, {
        "code": """
    boolean contains(Comment comment) {
        if (!comment.hasRange())
          return false;
        Range commentRange = comment.getRange().get();
        for (Comment c : getComments()) {
          if (!c.hasRange())
            return false;
          Range cRange = c.getRange().get();
          if (cRange.begin.equals(commentRange.begin) && cRange.end.line == commentRange.end.line && Math.abs(cRange.end.column - commentRange.end.column) < 2)
            return true;
        }
        return false;
    }
    """,
        "answer": """
    Based on the method signature and body, the instances of `comment` should be generated to test the API method, which represents whether or not it is included in its own Comments.
    To achieve high code coverage, diverse instances should be generated to reach different branches in the Method Body.
    Therefore, we can partition the following equivalence classes for `comment`:
    - class:
        1. `comment`: is null
    - class:
        1. `comment`: should has no range
    - class:
        1. `comment`: should has a range, and list of comments has at least one comment with a range that matches the given comment's range
    - class:
        1. `comment`: should has a range, and list of comments has at least one comment with a range that does not match the given comment's range
    """
    }, {
        "code": """
    boolean areInOrder(Node a, Node b, boolean ignoringAnnotations) {
        return compare(a, b, ignoringAnnotations) <= 0;
    }
    """,
        "answer": """
    Based on the method signature and body, the instances of `a`, `b`, and `ignoringAnnotations` should be generated to test the API method, which represents whether or not the two nodes are in order.
    To achieve high code coverage, diverse instances should be generated to reach different branches in the Method Body.
    Therefore, we can partition the following equivalence classes for `a`, `b`, and `ignoringAnnotations`:
    - class:
        1. `a`: is null; 2. `b`: can be any Node; 3. `ignoringAnnotations`: can be true or false
    - class:
        1. `b`: is null; 2. `a`: can be any Node; 3. `ignoringAnnotations`: can be true or false
    - class:
        1. `a`: is not null; 2. `b`: is not null, `a` is in order before `b`; 3. `ignoringAnnotations`: is true
    - class:
        1. `a`: is not null; 2. `b`: is not null, `a` is not in order before `b`; 3. `ignoringAnnotations`: is true
    - class:
        1. `a`: is not null; 2. `b`: is not null, `a` is in order before `b`; 3. `ignoringAnnotations`: is false
    - class:
        1. `a`: is not null; 2. `b`: is not null, `a` is not in order before `b`; 3. `ignoringAnnotations`: is false

    """
    }
]


if __name__ == "__main__":
    fewshot_prompt = create_prompt_for_partition_few_shot(EXAMPLE_MESSAGE , EXAMPLES)
    final_prompt = create_prompt_for_partition(SYSTEM_MESSAGE , fewshot_prompt , QUESTION_MESSAGE)
    llm = ChatOpenAI(model='qwen-coder-plus' , openai_api_key=API_KEY , openai_api_base=BASE_URL , max_tokens=1000 , temperature=0.0)
    # llm = ChatOpenAI(model='deepseek-ai/DeepSeek-V3' , openai_api_key=API_KEY , openai_api_base=BASE_URL , max_tokens=512 , temperature=0.0)
    # llm = ChatOpenAI(model='gpt-3.5-turbo', openai_api_key=API_KEY, openai_api_base=BASE_URL, max_tokens=1000, temperature=0.0)
    document_name = "equivalence_result_qwen"
    equivalencePartition = EquivalencePartitioning(llm , final_prompt)

    for root, dir, files in os.walk(CODE_DIR):
        for file in files:
            file_name = file
            with open(os.path.join(CODE_DIR, file), 'r', encoding="utf-8") as code_file:
                code = code_file.read()
                # print(code)
                code_file.close()
            # print(final_prompt)
            equivalencePartition.run(code, document_name, file_name)