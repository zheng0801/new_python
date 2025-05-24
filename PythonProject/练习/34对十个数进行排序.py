# 对10个数进行排序。

#方法一：
# str_list = [1, '4', '111', '12', '25', '4', '34', '56', '1234', '5']
# #推导式将列表中的str转成int类型
# int_list = [int(x) for x in str_list]
#
# #调用sort()方法进行排序list.sort(key=None, reverse=False) key：指定排序依据的函数
# # reverse：是否降序排序（默认 False 为升序） 返回值是None
# int_list.sort()
# print(int_list)
#
# #调用sorted()方法，sorted(iterable, key=None, reverse=False)，sorted()方法不会改变原列表顺序
# new_int_list = sorted(int_list, reverse=True)
# print(new_int_list)

# #方法二：
# #将输入的数据剪切并放到列表中
# str_list = input("请输入十个数用空格隔开：").split()
# #对列表中的数据进行转换
# int_list = [int(x) for x in str_list]
#
# #进行降序排序
# int_list.sort(reverse=True)
#
# for i in int_list:
#     print(i, end=' ')

str_list = map(int, input("请输入十个数用空格隔开：").split())#此时的str_list是 map 对象（迭代器）
# str_list = list(str_list)#需要转换成list才能进行sort()排序操作或直接使用sorted()
# str_list.sort()#sort() 是列表的方法，直接修改原列表，返回 None。
str_list = sorted(str_list)#sorted() 是内置函数，接受任何可迭代对象（包括 map），返回新列表

print(str_list)