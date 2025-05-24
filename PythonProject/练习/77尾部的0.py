# 给定一个整数n，计算出n!中尾部的0的个数

num = int(input('请输入一个整数：'))

# #方法一：
# def func(num):
#     sum = 1
#     while num != 0:
#         sum = sum * num
#         num -= 1
#     return sum
#
# flag = True
# count = 0
# sum = func(num)
# while flag:
#     if sum % 10 == 0:
#         count += 1
#         sum //= 10
#     else:
#         flag = False
#
# print(count)

#方法二：
def func(n):
    count = 0
    for i in range(5, n+1, 5):
        while i % 5 == 0:
            i //= 5
            count += 1
    return count

print(func(num))

