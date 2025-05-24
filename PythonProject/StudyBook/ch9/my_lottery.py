# 可以使⽤⼀个循环来理解中前述彩票⼤奖有多难。为此，创建⼀个名为 my_ticket 的列表或元组，再编写⼀个循
# 环，不断地随机选择数或字⺟，直到中⼤奖为⽌。请打印⼀条消息，报告执⾏多少次循环才中了⼤奖。

from random import choice

lists = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']
ticket = []
my_ticket = []
frequency = 0

while len(ticket) < 4 :
    #生成中奖号码列表
    number = choice(lists)
    ticket.append(number)
    # i += 1

while True:
    #循环知道我的号码和中奖号码一致
    frequency += 1
    my_ticket = []
    while len(my_ticket) < 4:
        #生成我的号码列表
        number = choice(lists)
        my_ticket.append(number)
        # i += 1

    if my_ticket == ticket:
        #判断是否中奖，中奖结束循环
        print(f'恭喜你中奖了，中奖号码是{my_ticket}')
        break
    else:
        print(f'您的号码是{my_ticket}')

