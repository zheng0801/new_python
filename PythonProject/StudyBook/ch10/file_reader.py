# from pathlib import Path
#
# # path = Path('D:\\360MoveData\\Users\\zhengyl\\Desktop\\python\\练习\\ch10\\pi_digits.txt')
# # contents = path.read_text()
# # print(contents)
#
# path = Path('pi_digits.txt')#相对路径打开文件
# contents = path.read_text().rstrip()
# print(contents)

with open('D:\\360MoveData\\Users\\zhengyl\\Desktop\\python\\练习\\ch10\\pi_digits.txt', 'r', encoding = 'utf-8') as f:
    '''绝对路径打开文件'''
    # content = f.read()#读取整个文件
    # print(content)

    # content = f.readline()#读取文件行信息
    # print(content)

    contents = f.readlines()#逐行读取文件内容，返回一个列表
    for line in contents:
        print(line)