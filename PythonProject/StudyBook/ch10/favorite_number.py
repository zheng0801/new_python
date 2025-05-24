# 编写⼀个程序，提⽰⽤户输⼊⾃⼰喜欢的数，并使⽤ json.dumps() 将这个数存储在⽂件中。再编写⼀个程序，从
# ⽂件中读取这个值，并打印如下消息。I know your favorite number! It's _____
#
# 将你在完成练习 10.11 时编写的两个程序合⽽为⼀。如果存储了⽤户喜欢的数，就向⽤户显⽰它，否则提⽰⽤
# 户输⼊⾃⼰喜欢的数并将其存储在⽂件中。运⾏这个程序两次，看看它是否像预期的那样⼯作。

import json
from pathlib import Path

# favorite_number = input('请输入你喜欢的数：')
#
# with open('favorite_number.json', 'w', encoding = 'utf-8') as file:
#     content = json.dumps(favorite_number)
#     file.write(content)
#
# with open ('favorite_number.json', 'r', encoding = 'utf-8') as file:
#     content = file.read()
#     favorite_number = json.loads(content)
#     print(f'I know your favorite number! It\'s {favorite_number}')

if Path('favorite_number.json').exists():
    with open('favorite_number.json', 'r', encoding='utf-8') as file:
        content = file.read()
        favorite_number = json.loads(content)
        print(f'I know your favorite number! It\'s {favorite_number}')
else:
    favorite_number = input('请输入你喜欢的数：')
    with open('favorite_number.json', 'w', encoding='utf-8') as file:
        content = json.dumps(favorite_number)
        file.write(content)