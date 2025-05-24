# 创建⼀个名为 sandwich_orders 的列表，其中包含各种三明治的名字，再创建⼀个名为 finished_sandwiches
# 的空列表。遍历列表 sandwich_orders，对于其中的每种三明治，都打印⼀条消息，如“I made your tuna sandwich.”，并将其移到列表
# finished_sandwiches 中。当所有三明治都制作好后，打印⼀条消息，将这些三明治列出来。

# sandwich_orders = ['ham','chicken','club','open','tuna']
# finished_sandwiches = []
#
# while sandwich_orders:
#     pop_sandwich = sandwich_orders.pop()
#     print(f'I made your {pop_sandwich} sandwich.')
#     finished_sandwiches.append(pop_sandwich)
#
# print(f'你要的三名字已经全部制作完成了：{finished_sandwiches}')

# 使⽤为练习 7.8 创建的列表sandwich_orders，并确保 'pastrami' 在其中⾄少出现了三次。
# 在程序开头附近添加这样的代码：先打印⼀条消息，指出熟⾷店的五⾹烟熏⽜⾁（pastrami）卖完了；再使⽤⼀个 while 循环将列表
# sandwich_orders 中的 'pastrami' 都删除。确认最终的列表finished_sandwiches 中未包含 'pastrami'。

sandwich_orders = ['ham','pastrami','chicken','pastrami','club','open','pastrami','tuna']
finished_sandwiches = []

while sandwich_orders:
    pop_sandwich = sandwich_orders.pop()
    if pop_sandwich != 'pastrami':
        finished_sandwiches.append(pop_sandwich)
    print(f'I made your {pop_sandwich} sandwich.')

print(f'你要的三名字已经全部制作完成了：{finished_sandwiches}')