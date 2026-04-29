import os
from openai import OpenAI

# 初始化客户端（核心配置：替换为你的API Key）
client = OpenAI(
    api_key="sk-56bed7f0aa6944e3bd9d15ac227f9ca8",  # 也可以通过环境变量配置api_key=os.environ.get('DEEPSEEK_API_KEY')
    base_url="https://api.deepseek.com"  # DeepSeek 固定域名
)
try:
    response = client.chat.completions.create(
        model="deepseek-chat",  # 指定模型，可选 deepseek-chat / deepseek-reasoner
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},  # 系统角色定义
            {"role": "user", "content": "Hello"},  # 用户提问
        ],
        stream=False  # 非流式输出（一次性返回完整结果）
    )
    # 打印回复内容
    print("回复结果：", response.choices[0].message.content)
except Exception as e:
    print("调用失败：", str(e))