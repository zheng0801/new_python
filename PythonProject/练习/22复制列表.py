# 将一个列表的数据复制到另一个列表中。
import copy

list = [1,2,3,4,5,6,7,8,9,10]

#浅复制，list的数据变化了list1中的也会修改
# list1 = list
# list[0] = 5

#方法一：使用切片复制列表
list1 = list[:]

#方法二：
list2 = copy.copy(list)

list[0] = 5

print(list1)
print(list2)