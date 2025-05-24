# 编写⼀个 while 循环，提⽰⽤户输⼊其名字。收集⽤户输⼊的所有名字，将其写⼊ guest_book.txt，并确保这个⽂件中
# 的每条记录都独占⼀⾏。

with open('guest_book.txt', 'a', encoding = 'utf-8') as file:

    names = []

    while True:
        #生成名字列表
        name = input('请输入名字（以q结束）：')
        if name == 'q':
            break
        else:
            names.append(f"{name}\n")

    # for name in names:
    #     #写入文件
    #     file.write(f"{name}\n")
    file.writelines(names)
