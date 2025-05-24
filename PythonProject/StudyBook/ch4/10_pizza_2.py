# 在你为练习 4.1 编写的程序中，创建⽐萨列表的副本，并将其赋给变量 friend_pizzas，再完成如下任务。
# 在原来的⽐萨列表中添加⼀种⽐萨。在列表 friend_pizzas 中添加另⼀种⽐萨。
# 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使⽤⼀个 for 循环来打印第⼀个列表；
# 打印消息“My friend's favorite pizzas are:”，再使⽤⼀个 for 循环来打印第⼆个列表。核实新增的⽐萨被添加到了正确的列表中。


pizzas = ['margherita','napoletana','alla diavola','calzones']
friend_pizzas = pizzas[:]
friend_pizzas.append('fugazetta')

for pizza in pizzas:
    print(f'My favorite pizzas are:{pizza.title()}')

for pizza in friend_pizzas:
    print(f'My friend\'s favorite pizzas are:{pizza.title()}')