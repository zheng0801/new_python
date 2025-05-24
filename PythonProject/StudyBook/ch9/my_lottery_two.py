from random import choice

lists = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e']
tickets = ''
my_tickets = ''
frequency = 0

while len(tickets) < 4:
    '''生成中奖号码'''
    ticket = choice(lists)
    tickets = f'{tickets}{ticket}'

while True:
    '''循环比对是否中奖'''
    frequency += 1 #统计比对次数
    while len(my_tickets) < 4:
        '''生成我的号码'''
        ticket = choice(lists)
        my_tickets = f'{my_tickets}{ticket}'

    if my_tickets == tickets:
        print(f'恭喜你第{frequency}次中奖了，中奖号码是{my_tickets}')
        break
    else:
        print(f'你的号码是{my_tickets}')

    my_tickets = ''