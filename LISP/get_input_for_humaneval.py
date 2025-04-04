import os
import re

TEST_CASE_DIR = os.path.join(os.getcwd() , "HumanEval_result" , "input_generation")
TEST_TARGET_DIR = os.path.join(os.getcwd() , "HumanEval_test_case")

text = """
Some code here.
'''java
public class Test {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
'''
More code here.
"""

# 正则表达式：匹配以 '''java 开头，''' 结尾的内容
pattern = r"```java(.*?)```"

# 使用 re.search 或 re.findall 查找匹配部分
# matches = re.findall(pattern, text, re.DOTALL)

# # 输出匹配结果
# print("匹配到的内容：")
# for match in matches:
#     print(match)

for dir_name in os.listdir(TEST_CASE_DIR):
    dir_path = os.path.join(TEST_CASE_DIR , dir_name)
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path , file)
        with open(file_path , 'r' , encoding="utf-8") as code_file:
            content = code_file.read()
            matches = re.findall(pattern, content , re.DOTALL)
            code_file.close()
        with open(os.path.join(TEST_TARGET_DIR , dir_name.split('result')[0] + file + '_Test') , 'w' , encoding="utf-8") as target_file:
            code_content = ""
            for match in matches:
                code_content += match
            target_file.write(code_content.strip('\n'))
            target_file.close()
    break

