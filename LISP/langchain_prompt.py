
from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate , SystemMessagePromptTemplate


API_KEY = "sk-SD3QkuWcKeF8cLAjZel0kn2scMyycuOQFiuVyTRsPNOuy1FP"
BASE_URL = "https://api.chatanywhere.tech/v1"

# def get_completion(system_message , prompt , api_to_partiton,
#                    model="gpt-3.5-turbo"):
#     client = OpenAI(api_key=API_KEY,base_url=BASE_URL)
#
#     # messages = [
#     #     {"role" : "system" , "content" : system_message},
#     #     {"role" : "user" , "content" : prompt}
#     # ]
#
#     system_message_template = SystemMessagePromptTemplate.from_template("")
#
#     responses = client.chat.completions.create(
#         model = model,
#         messages = messages,
#         temperature = 0.3,
#         max_tokens=500,
#         logprobs=True
#     )
#
#     file_content = responses.choices[0].message.content
#     print(file_content)

# SYSTEM_MESSAGE = '''
# You are an experienced tester. Now you are expected to partition the equivalence classes of the test inputs for the provided API method.
# In each class, your answer should start with "- class:" and specify the form of each parameter.
# '''
#
# system_message_template = ChatPromptTemplate.from_template(SYSTEM_MESSAGE)
#
# print(system_message_template)
#
# QUESTION_MESSAGE = [
#     ("human" , "API Method: ```java {code}```"),
#     ("AI" , "Answer : Let's do this step by step. ")
# ]
#
# EXAMPLE_MESSAGE = [
#     ("human" , "API method: ```java {code}```"),
#     ("AI" , "Answer : Let's do this step by step. {answer}")
# ]
#
# # human_message_template = HumanMessagePromptTemplate.from_template(EXAMPLE_MESSAGE)

system_message_template = SystemMessagePromptTemplate.from_template("You are a helpful assistant.")
print(system_message_template)

human_message_template = HumanMessagePromptTemplate.from_template(
    "What is the capital of {country}? The currency is {currency}."
)
print(human_message_template)

for message in system_message_template:
    print(message)

# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system", system_message_template),
#     ("user", human_message_template)
# ])
#
# prompt = chat_prompt.format_messages(country="France", currency="Euro")
#
# print(prompt)