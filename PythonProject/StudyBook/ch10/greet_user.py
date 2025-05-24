
import json

with open('username.json', 'r', encoding = 'utf-8') as file:
    contents = file.read()
    username = json.loads(contents)

print(f'欢迎回来：{username.title()}')