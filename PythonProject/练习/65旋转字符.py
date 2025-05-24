# 字符串旋转:给定两字符串A和B，如果能将A从中间某个位置分割为左右两部分字符串(可以为空串)，并
# 将左边的字符串移动到右边字符串后面组成新的字符串可以变为字符串B时返回true。

str_a = input('请输入第一个字符串：')
str_b = input('请输入第二个字符串：')

# #方法一：
# #定义一个函数，实现将字符串切割重连并喝另一字符串对比
# def func(str_a, str_b):
#     for i in range(len(str_a) - 1):
#         left_str_a = str_a[:i+1]
#         right_str_a = str_a[i + 1:]
#         new_str_a = right_str_a + left_str_a
#         if new_str_a == str_b:
#             return True
#
# print(func(str_a, str_b))

#方法二：
#定义一个函数对比两个字符串长度，长度一致后，通过b是否包括在a+a中来判断a是否可以切割后拼接成b
def func(a, b):
    if len(a) != len(b):
        return False
    else:
        bigA = a + a
        result = b in bigA
        return result

print(func(str_a, str_b))