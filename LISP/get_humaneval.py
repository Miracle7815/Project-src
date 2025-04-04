import os
import shutil
import re

JAVA_PATH = os.path.join("D:\\" , "human-eval-java-main" , "src" , "main" , "java" , "humaneval" , "correct")
TARGET_DIR = os.path.join(os.getcwd() , "HumanEval")
# print(TARGET_DIR)

# 将注释去除
line_comment_pattern = r"//.*"
block_comment_pattern = r"/\*.*?\*/"

# code_string = """
# int a = 10;  // This is a line comment
# int b = 20;  /* This is a block comment */
# int c = 30;  // Another line comment
# /* This is another block comment */
# """

# # 替换掉所有行注释
# code_string_no_line_comments = re.sub(line_comment_pattern, '', code_string)
#
# # 替换掉所有块注释
# code_string_no_comments = re.sub(block_comment_pattern, '', code_string_no_line_comments, flags=re.DOTALL)
#
# # 输出去除注释后的代码
# print("Code without comments:")
# print(code_string_no_comments)

for root , dir , files in os.walk(JAVA_PATH):
    for file in files:
        # print(os.path.join(root , file))
        SOURCE_FILE_PATH = os.path.join(root , file)
        # shutil.copy(SOURCE_FILE_PATH , TARGET_DIR)
        with open(SOURCE_FILE_PATH , encoding="utf-8") as code_file:
            content = code_file.read()
            code_file.close()
        temp = re.sub(line_comment_pattern , '' , content)
        code_no_comment = re.sub(block_comment_pattern , '', temp , flags=re.DOTALL)
        lines = ""
        for line in code_no_comment.split('\n'):
            if line != '':
                lines += line + '\n'
        # print(lines)
        with open(os.path.join(TARGET_DIR , file) , 'w' , encoding="utf-8") as code_file:
            code_file.write(lines)
            code_file.close()

