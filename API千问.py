from openai import OpenAI
import os

def get_response():
    client = OpenAI(
        api_key="sk-9908e8d1bf8243b3b941d9fd3d6429d6",  #  API Key
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # base_url
    )
    completion = client.chat.completions.create(
        model="qwen-plus",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[{'role': 'system', 'content': 'You are a helpful assistant.'},
                  {'role': 'user', 'content': '你是谁？'}]
        )
    # json 数据
    #print(completion.model_dump_json())
    print(completion.choices[0].message.content)

if __name__ == '__main__':
    get_response()