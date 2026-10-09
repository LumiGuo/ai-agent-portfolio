import os
from openai import OpenAI

client=OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY","sk-ws-H.PERLHLH.ytFo.MEUCIQDOkABhvRi5PIbAogt0AAb3J59LWoIT-aKguJg4ajpXIAIgVbZxucFEZdDXTAVZb19Dzxr89uJDqzhDagAJQnXGnCk"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
resp=client.chat.completions.create(
    model="qwen-plus",
    messages=[{"role":"user","content":"用一句话解释什么是负载均衡"}],
)

print(resp.choices[0].message.content)