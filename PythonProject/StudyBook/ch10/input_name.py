# 编写⼀个程序，提⽰⽤户输⼊其名字。在⽤户做出响应后，将其名字写⼊⽂件 guest.txt。

with open('guest.txt', 'w', encoding = 'utf-8') as file:
    name = input('请输入名字：')
    file.write(name)