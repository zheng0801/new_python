#编写程序找出100以内的奇数并打印

# list = []
#
# for i in range(1,101):
#     #通过对二取余不等于0判断出奇数
#     if i % 2 != 0:
#         list.append(i)
#
# print(list)

list2 = []

#直接通过range（）函数从一开始每两个数取一个
for i in range(1,100,2):
    list2.append(i)

print(list2)