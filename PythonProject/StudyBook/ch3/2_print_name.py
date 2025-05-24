# 将⼀些朋友的姓名存储在⼀个列表中，并将其命名为names。依次访问该列表的每个元素，从⽽将每个朋友的姓名都打印出来。

names = ['张三','李四','王五','赵六','林七']

# for i in range(len(names)):
#     print(names[i])

# for name in names:
#     print(name)

for i in range(len(names)):
    print(f"{names[i]}你好，今天是周四")
