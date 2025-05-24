# 编写程序，找出所有的水仙花数:
# 水仙花数:是一个三位数，各位数字立方和等于该数字本身。

import math

list = []

for i in range(100, 1000):
    num1 = i // 100#通过取整拿到百位
    num2 = (i % 100) // 10#通过求100的余数在取整拿到十位
    num3 = i % 10#通过对10求余拿到个位
    if pow(num1, 3) + pow(num2, 3) + pow(num3, 3) == i:
        list.append(i)

    # if (num1**3 + num2**3 + num3**3) == i:
    #     list.append(i)

for i in list:
    print(f'{i}是水仙花数', end=' ')