# 实现猜数字游戏。

import random

num = random.randint(1, 100)#randint()包含两边的值，所以取值范围是[1, 100]
print(num)

# number = int(input('请输入所猜测的数字：'))
#
# #方法一：使用for循环
# for i in range(1000):
#     if number == num:
#         print(f'恭喜你猜对了，{number}就是答案')
#         break
#     else:
#         if number > num:
#             number = int(input('你输入的数太大了，请重新输入'))
#         else:
#             number = int(input('你输入的数太小了，请重新输入'))

times = 7
print('开始猜数字游戏，请输入一到一百的整数')
while times != 0:
    number = int(input('请输入所猜测的数字：'))
    if number > num:
        print('您输入的数字有点大了，请继续猜')
    elif number < num:
        print('您输入的数字有点小了，请继续猜')
    elif number == num:
        print(f'恭喜您猜对了{number}就是答案')
        break
    times -= 1

if times == 0:
    print('游戏结束，您猜了七次都没猜对')
