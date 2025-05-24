# 求1+2!+3!+...+20!的和。
import math

#方法一：
# sum = 0
#
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# for i in range(1, 21):
#     sum += factorial(i)
#
# print(sum)

#方法二：
sum = 0

for i in range(1, 21):
    sum += math.factorial(i)

print(sum)
