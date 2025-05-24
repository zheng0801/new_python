# 编写程序，输入三个数，从小到大输出三个数。

num1 = int(input('请输入第一个数：'))
num2 = int(input('请输入第二个数：'))
num3 = int(input('请输入第三个数：'))

#方法一：用if语句判断
# list = []
#定义一个比较大小的函数并返回较大的数
# def compare(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
# if compare(num1, num2) == num1:
#     if compare(num1, num3) == num1:
#         list.append(num1)
#         if compare(num2, num3) == num2:
#             list.append(num2)
#             list.append(num3)
#         else:
#             list.append(num3)
#             list.append(num2)
#     else:
#         list.append(num3)
#         list.append(num1)
#         list.append(num2)
# else:
#     if compare(num2, num3) == num2:
#         list.append(num2)
#         if compare(num1, num3) == num1:
#             list.append(num1)
#             list.append(num3)
#         else:
#             list.append(num3)
#             list.append(num1)
#     else:
#         list.append(num3)
#         list.append(num2)
#         list.append(num1)

list = [num1, num2, num3]

#方法二：使用sort()
#sort()是一个用于对列表进行原地排序的方法，list.sort(key=None, reverse=False)，仅用于列表
# key（可选）：指定一个函数，用于从列表的每个元素中提取比较键
# reverse（可选）：布尔值，如果设为 True，则按降序排序
# list.sort(reverse=True)

# for i in range(len(list)):
#     print(list.pop())


#方法三：使用sorted()
#sorted()返回排序后的新列表，任意可迭代对象都可用（列表、元组等）
#sorted(iterable, key=None, reverse=False)，iterable：要排序的可迭代对象（如列表、元组、字符串等）
list1 = sorted(list, reverse=True)

# for i in range(len(list1)):
#     print(list1.pop())
print(f'三个数由小到大分别是：{list1[2]}、{list1[1]}、{list1[0]}')