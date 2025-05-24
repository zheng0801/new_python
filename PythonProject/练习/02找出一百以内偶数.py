#编写程序找出100以内的偶数并打印

# for i in range(1,101):
#     #%用于求余，当余数等于0是是偶数
#     if i % 2 == 0:
#         print(i)

list = []

for i in range(1,100):
    if i % 2 == 0:
        #将判断出的偶数添加到列表中
        list.append(i)
        #将要添加的数据添加到索引为0的列表中，实现倒叙显示
        # list.insert(0,i)

print(list)