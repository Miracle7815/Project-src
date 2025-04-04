from langchain.prompts import FewShotChatMessagePromptTemplate , ChatPromptTemplate
from langchain.schema import LLMResult
import os
from langchain.chat_models import ChatOpenAI
from function_file import write_result , create_prompt_for_partition , create_prompt_for_partition_few_shot

# 控制台
# API_KEY = "sk-SD3QkuWcKeF8cLAjZel0kn2scMyycuOQFiuVyTRsPNOuy1FP"
# BASE_URL = "https://api.chatanywhere.tech/v1"

# 免费apikey
# API_KEY = "sk-YXeIf5Hzq452SluTP77QPGWOeWHq7GFMqH4C4kwr9uFZhbhv"
# BASE_URL = "https://api.openai-proxy.org/v1"

#deep seek
API_KEY = "sk-a89d7bc99b7344a7826c0291520de73c"
BASE_URL = "https://api.deepseek.com"

#Qwen
# API_KEY = "sk-3d786e7826bf4ffdbe0e9d73e07c8619"
# BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

class EquivalencePartitioning:
    def __init__(self , llm , prompt):
        self.llm = llm
        self.prompt = prompt

    def parse_result(self , result: LLMResult , document_name , file_name):
        # print(type(result))
        text = result.generations[0][0].text
        write_result(document_name , file_name , text)

    def run(self , code , document_name , file_name):
        messages = self.prompt.format_messages(code=code)
        for message in messages:
            print(f"\33[32m{message.content}\033[0m\n")
        llm_result: LLMResult = self.llm.generate([messages])
        self.parse_result(llm_result , document_name , file_name)


SYSTEM_MESSAGE = '''
You are an experienced tester. Now you are expected to partition the equivalence classes of the test inputs for the provided API method.
In each class, your answer should start with "- class:" and specify the form of each parameter.
'''

QUESTION_MESSAGE = [
    ("human", "API Method: ```java {code}```"),
    ("ai", "Anwser: Let's do this step by step. "),
]

EXAMPLE_MESSAGE = [
    ("human", "API Method: ```java {code}```"),
    ("ai", "Anwser: Let's do this step by step. {answer}"),
]

EXAMPLES = [
    {
        "code": """
    TimeZone getGmtTimeZone(final String pattern) {
        if ("Z".equals(pattern) || "UTC".equals(pattern)) {
            return GREENWICH;
        }

        final Matcher m = GMT_PATTERN.matcher(pattern);
        if (m.matches()) {
            final int hours = parseInt(m.group(2));
            final int minutes = parseInt(m.group(4));
            if (hours == 0 && minutes == 0) {
                return GREENWICH;
            }
            return new GmtTimeZone(parseSign(m.group(1)), hours, minutes);
        }
        return null;
    }
    """,
        "answer": """
    Based on the method signature and body, the instances of `pattern` should be generated to test the API method, which represents time zones.
    To achieve high code coverage, diverse instances should be generated to reach different branches in the Method Body.
    Therefore, we can partition the following equivalence classes for `pattern`:
    - class:
        1. `pattern`: Z or UTC
    - class:
        1. `pattern`: does not match GMT_PATTERN
    - class:
        1. `pattern`: matches GMT_PATTERN, and both its hour part and minute part are 0
    - class:
        1. `pattern`: matches GMT_PATTERN, and its hour part or minute part is not 0
    """
    },
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
    llm = ChatOpenAI(model='deepseek-chat' , openai_api_key=API_KEY , openai_api_base=BASE_URL , max_tokens=1000 , temperature=0.0)
    document_name = "equivalence_result"
    file_name = "example_result_0.0_2"
    equivalencePartition = EquivalencePartitioning(llm , final_prompt)

    code = """
    boolean equalsIgnoreMissingFractionDigits(double accurate, double approximate) {
      final double delta = Math.abs(accurate - approximate);
      if (delta < 1) {
        int p = Numerics.toExp10(MathFunctions.getExponent(delta));
        p = Math.max(p - (EXPONENT_FOR_ZERO + 1), 0);
        if (p+1 < POW10.length && POW10[p+1] <= delta) p++;
        p = (-2*EXPONENT_FOR_ZERO - 3) - p;
        if (p >= 0 && p < POW10.length) {
          double scale = POW10[p];
          assert delta*scale >= 0.1 : delta;
          final double diffInFractions = approximate * scale;
          approximate = Math.rint(diffInFractions);
          if (Math.abs(approximate - diffInFractions) <= Math.ulp(diffInFractions)) {
            while (approximate % 10 == 0 && scale >= 10) {
              approximate /= 10;
              scale /= 10;
            }
            accurate *= scale;
            return Math.abs(approximate - accurate) <= 0.5;
          }
        }
      }
      return Double.doubleToLongBits(accurate) == Double.doubleToLongBits(approximate);
    }
        """

    equivalencePartition.run(code , document_name, file_name)
