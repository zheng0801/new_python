# 有一个已经排好序的列表。现输入一个数要求按原来的规律将它插入数组中。

list = [-3, 5, 8, 12, 34, 56]

num = int(input('请输入一个数：'))

list.append(num)
list.sort()
print(list)