# 创建⽂件 cats.txt 和 dogs.txt，在第⼀个⽂件中⾄少存储三只猫的名字，在第⼆个⽂件中⾄少存储三条狗的名字。编写⼀
# 个程序，尝试读取这些⽂件，并将其内容打印到屏幕上。将这些代码放在⼀个 try-except 代码块中，以便在⽂件不存在时捕获
# FileNotFoundError 异常，并显⽰⼀条友好的消息。将任意⼀个⽂件移到另⼀个地⽅，并确认 except 代码块中的代码将正确地执⾏。
# 修改你在练习 10.8 中编写的 except 代码块，让程序在⽂件不存在时静默失败。

# with open('cats.txt', 'a', encoding = 'utf-8') as file_two:
#     '''追加cats的名字'''
#     cats = ['小锅', '可可', '初一']
#     for cat in cats:
#         file_two.write(f'{cat}\n')
#
# with open('dogs.txt', 'a', encoding = 'utf-8') as file_one:
#     '''追加dogs的名字'''
#     dogs = ['小白', '小黑', '小黄']
#     for dog in dogs:
#         file_one.write(f'{dog}\n')


try:
    with open('cats.txt', 'r', encoding = 'utf-8') as file_one:
        #读取打印cat名字
        cat_names = file_one.readlines()
        print(cat_names)
# except FileNotFoundError:
#     print('文件不存在')
except:
    pass

try:
    with open('dogs.txt', 'r', encoding = 'utf-8') as file_two:
        #读取打印dog名字
        dog_names = file_two.readlines()
        print(dog_names)
# except FileNotFoundError:
#     print('文件不存在')
except:
    pass