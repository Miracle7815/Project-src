import requests
import json
url = "https://api.openai-proxy.org/v1/chat/completions"
payload = {
    "model": "gpt-3.5-turbo",
    # "messages": [
    #     {"role": "user", "content": "Please introduce Nanjing University"}
    # ],
    "messages": [
        {"role": "user", "content": "Please introduce Nanjing University"}
    ],
    "max_tokens": 200,
    "temperature": 0.4
}
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-YXeIf5Hzq452SluTP77QPGWOeWHq7GFMqH4C4kwr9uFZhbhv"
}

res = requests.post(url, data=json.dumps(payload), headers=headers)
# res = requests.post(url, json=payload , headers=headers)
print(res)
if res.status_code == 200:
    result = res.json()
    # 方法1：直接提取第一个choice的content
    reply = result['choices'][0]['message']['content']
    print("ChatGPT回答：", reply)

    # 方法2：安全提取（带错误处理）
