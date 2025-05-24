# 打印出杨辉三角

#方法一：
list = []

for i in range(9):
    #创建一个空列表，存放每行的数据
    row = []
    if i == 0:#添加第一行的数据
        row.append(1)
    elif i == 1:#添加第二行的数据
        row.append(1)
        row.append(1)
    else:#令每行的开头的1
        row.append(1)
        for j in range(1, i):#计算每行中间项的值
            row.append(list[i-1][j-1]+list[i-1][j])
        row.append(1)#令最后一项的值的1
    list.append(row)#将行列表添加到总列表中

#循环打印列表
for i in list:
    for j in i:
        print(j, end=' ')
    print()

# #方法二：
# a = []
#
# #往列表中添加列表，并将列表的第一个元素和最后一个元素添加1
# for i in range(10):
#     a.append([])
#     for j in range(10):
#         a[i].append(1)
#     # a[i][0] = 1
#     a[i][i] = 1
#
# #计算出每个列表中中间元素的值
# for i in range(2, 10):
#     for j in range(1, i):
#         a[i][j] = a[i-1][j] + a[i-1][j-1]
#
# #循环打印出列表的值
# for i in range(10):
#     for j in range(i+1):
#         print(a[i][j], end=' ')
#     print()
