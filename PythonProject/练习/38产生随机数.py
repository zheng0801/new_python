# 编写程序，生成随机数

import random

num = f'{random.random():.2f}'
num2 = random.randint(1, 100)
num3 = random.randrange(1, 100, 10)

print(num)
print(num2)
print(num3)