# 按相反的顺序输出列表的值。

list = ['a', 'b', 'c', '1', '2', '3', '中']

# #方法一：切片翻转
# list1 = list[::-1]
#
# print(list)
# print(list1)

#方法二：调用内置方法，将原有列表的元素逆转顺序
list.reverse()

print(list)