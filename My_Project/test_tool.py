from openai import OpenAI
import json

API_KEY = "sk-YXeIf5Hzq452SluTP77QPGWOeWHq7GFMqH4C4kwr9uFZhbhv"
BASE_URL = "https://api.openai-proxy.org/v1"

# API_KEY = "sk-3d786e7826bf4ffdbe0e9d73e07c8619"
# BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# messages = [{"role": "user", "content": "Please introduce Nanjing University"}]
# client = OpenAI(api_key=API_KEY,base_url=BASE_URL)
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=messages,
#     temperature=0,
#     max_tokens=300
# )
# print(response.choices[0].message.content)
def get_weather(location: str) -> dict:
    weather_data = {
        "San Francisco": {"temp": 22, "unit": "Celsius"},
        "Beijing": {"temp": 15, "unit": "Celsius"},
    }
    return weather_data.get(location, {"error": "Location not found"})


client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

user_input = "旧金山现在的气温是多少？"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_input}],
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "获取某地的当前天气",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "城市名称"}
                },
                "required": ["location"]
            }
        }
    }],
    tool_choice="auto",  # 由模型决定是否调用工具
)

print(f'response: {response.choices[0].message.content}')
tool_call = response.choices[0].message.tool_calls[0]
print(f'tool_call: {tool_call}')
func_name = tool_call.function.name
print(f'func_name: {func_name}')
args = json.loads(tool_call.function.arguments)
print(f'args: {args}')


# 执行工具
if func_name == "get_weather":
    weather_result = get_weather(location=args["location"])

    second_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": None, "tool_calls": [tool_call]},
        # {"role": "tool", "content": str(weather_result), "name": func_name},
        {"role": "tool", "content": str(weather_result), "tool_call_id": tool_call.id},
    ],
    )

    print(second_response.choices[0].message.content)
