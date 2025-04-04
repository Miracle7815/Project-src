from langchain.prompts import FewShotChatMessagePromptTemplate , ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.schema import LLMResult
import os
from langchain.chat_models import ChatOpenAI


def write_result(document_name , file_name , content):
    RESULT_FILE = os.getcwd()
    # RESULT_PATH = os.path.join(RESULT_FILE , "result" , document_name , file_name)
    RESULT_PATH = os.path.join(RESULT_FILE, "deepseek_result", document_name, file_name)
    with open(RESULT_PATH , 'w' ,  encoding='utf-8') as write_file:
        write_file.write(content)
    write_file.close()

def write_result_for_humaneval(document_name , file_name , content):
    RESULT_FILE = os.getcwd()
    # RESULT_PATH = os.path.join(RESULT_FILE , "result" , document_name , file_name)
    RESULT_PATH = os.path.join(RESULT_FILE, "Humaneval_result", document_name, file_name)
    with open(RESULT_PATH , 'w' ,  encoding='utf-8') as write_file:
        write_file.write(content)
    write_file.close()


def create_prompt_for_partition_few_shot(example_message , example):
    # few_shot_template = ""
    # for example in example_list:
    #     template = "API Method: ```java " + example["code"] + "```\n"
    #     answer = "Answer: Let's do this step by step." + example["answer"]
    #     few_shot_template += template + answer
    # print(few_shot_template)
    # print(ChatPromptTemplate.from_messages(example_message))

    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=ChatPromptTemplate.from_messages(example_message),
        examples=example
    )

    # print(few_shot_prompt)
    return few_shot_prompt


def create_prompt_for_partition(system_message , fewshot_prompt , question_message):
    # role_human = "human"
    # prompt = "API Method: ```java \n" + code + "\n```"
    # role_ai = "ai"
    # answer = "Answer: Let's do this step by step"
    # print(prompt)
    # print(answer)

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system" , system_message),
            fewshot_prompt
        ] + question_message
    )

    # print(final_prompt)
    return final_prompt

def create_prompt_for_input_generation_few_shot(example_message , example):
    # few_shot_template = ""
    # for example in example_list:
    #     template = "API Method: ```java " + example["code"] + "```\n"
    #     answer = "Answer: Let's do this step by step." + example["answer"]
    #     few_shot_template += template + answer
    # print(few_shot_template)
    # print(ChatPromptTemplate.from_messages(example_message))

    few_shot_prompt = FewShotChatMessagePromptTemplate(
        example_prompt=ChatPromptTemplate.from_messages(example_message),
        examples=example
    )

    # print(few_shot_prompt)
    return few_shot_prompt

def create_prompt_for_input_generation(system_message , fewshot_prompt , question_message):
    # role_human = "human"
    # prompt = "API Method: ```java \n" + code + "\n```"
    # role_ai = "ai"
    # answer = "Answer: Let's do this step by step"
    # print(prompt)
    # print(answer)

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system" , system_message),
            fewshot_prompt
        ] + question_message
    )

    # print(final_prompt)
    return final_prompt