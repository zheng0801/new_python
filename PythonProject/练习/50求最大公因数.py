# 求两个数的最大公因数。

num1 = int(input('请输入第一个数：'))
num2 = int(input('请输入第二个数：'))

# #方法一：
# num3 = 0
# num4 = num2
# sum = 0
#
# #判断数奇偶，偶数返回0，奇数返回1
# def even_number(num):
#     if num % 2 == 0:
#         return 0
#     else:
#         return 1
#
# #定义一个判断大小的函数，前数大返回True
# def magnitude_number(num1, num2):
#     if num1 > num2:
#         return True
#     elif num1 < num2:
#         return False
#
# if num1 == num2:
#     num3 = num1
# else:
#     # 判断是否均为偶数，均为偶数则除2取整，知道有数不为偶数，并统计除法计算次数
#     while even_number(num1) == 0 and even_number(num2) == 0:
#         num1 /= 2
#         num2 /= 2
#         sum += 1
#
#     # 当差不等于小数时循环
#     while num3 != num2:
#         # 将上一轮循环的小数赋值给num2
#         num2 = num4
#         # 计算差num3的值
#         if num1 > num2:
#             num3 = num1 - num2
#         else:
#             num3 = num2 - num1
#
#         # 将小数赋值给num1做下一轮的大数，将差赋值给num4
#         if magnitude_number(num1, num2) == True:
#             num1 = num2
#             num4 = num3
#         else:
#             num1 = num1
#             num4 = num3
#
# #计算公约数
# if sum == 0:
#     count = num3
# else:
#     count = sum * 2 * num3
#
# print(f'最大公约数是：{int(count)}')

# #方法二：
# def func1(a, b):
#     if a == b:
#         return a
#     num = min(a, b)
#     while a % num != 0 or b % num != 0:
#         num -= 1
#     return num

#方法三
def func2(a, b):
    while b != 0:
        a, b = b, a%b
    return a

print(func1(num1, num2))
print(func2(num1, num2))


