# 编写⼀个函数，它接受顾客要在三明治中添加的⼀系列⾷材。这个函数只有⼀个形参（它收集函数调⽤中提供的所有
# ⾷材），并打印⼀条消息，对顾客点的三明治进⾏概述。调⽤这个函数三次，每次都提供不同数量的实参。

def sandwich_ingredient(*foods):
    print(f'顾客的三明治添加了：{foods}')

sandwich_ingredient('火腿', '芝士', '番茄')
sandwich_ingredient('牛肉')
sandwich_ingredient('芝士', '虾仁')