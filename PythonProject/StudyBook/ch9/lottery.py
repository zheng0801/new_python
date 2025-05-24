# 创建⼀个列表或元素，其中包含 10 个数和 5 个字⺟。从这个列表或元组中随机选择 4 个数或字⺟，并打印⼀条消息，
# 指出只要彩票上是这 4 个数或字⺟，就中⼤奖了。

from random import choice

lists = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']
i = 1
win_number = ''
numbers = input('请输入一个四位数的号码：')

while i <= 4:
    number = choice(lists)
    win_number = f'{win_number}{number}'
    i += 1

if numbers == win_number:
    print('恭喜你中奖了')
else:
    print(f'中奖号码是{win_number}，您没有中奖')


