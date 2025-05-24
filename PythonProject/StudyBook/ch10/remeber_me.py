
import json
from pathlib import Path

# username = input('请问您的名字是？')

# with open('username.json', 'w', encoding = 'utf-8') as file:
#     '''存储json格式的名字到文件中'''
#     username_json = json.dumps(username)
#     file.write(username_json)
#
# print(f'欢迎回来{username.title()}')

# try:
#     with open('username.json', 'r', encoding='utf-8') as file:
#         '''读取json格式的数据转换并打印'
#         contents = file.read()
#         username = json.loads(contents)
#         print(f'欢迎回来：{username.title()}！')
# except FileNotFoundError:
#     username = input('请问您的名字是？')
#     with open('username.json', 'w', encoding='utf-8') as file:
#         '''创建文件并存储json格式的名字'''
#         username_json = json.dumps(username)
#         file.write(username_json)
#         print(f'欢迎回来：{username.title()}！')

# if Path('username.json').exists():
#     #判断是否存在文件，存在则读取文件内容并打印
#     with open('username.json', 'r', encoding='utf-8') as file:
#         contents = file.read()
#         username = json.loads(contents)
#         print(f'欢迎回来：{username.title()}！')
# else:
#     #文件不存在则创建文件并输入数据存到文件中
#     username = input('请问您的名字是？')
#     with open('username.json', 'w', encoding='utf-8') as file:
#         username_json = json.dumps(username)
#         file.write(username_json)
#         print(f'欢迎回来：{username.title()}！')


def get_store_username(path):
    '''如果存储用户名则获取它'''
    if Path(path).exists():
        with open(path, 'r', encoding = 'utf-8') as file:
            content = file.read()
            username = json.loads(content)
        return username
    else:
        return None

def greet_user():
    '''问候用户并打印名称'''
    username = get_store_username('username.json')
    if username:
        print('欢迎回来：')
        for key in username.keys():
            print(f'{key}：{username[key]}')
    else:
        peoples = {}
        username = input('请问您的名字是？')
        peoples['姓名'] = username
        userage = input('请问您的年龄是？')
        peoples['年龄'] = userage
        userheigth = input('请问您的身高是？')
        peoples['身高'] = userheigth
        with open('username.json', 'w', encoding='utf-8') as file:
            username_json = json.dumps(peoples)
            file.write(username_json)
            print(f'欢迎回来：{username.title()}！')

greet_user()