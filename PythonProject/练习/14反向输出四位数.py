# 编写程序，输入一个四位整数，反向输出对应四位数。

num = int(input('请输入一个四位整数：'))

# #方法一：
# num1 = num // 1000
# num2 = num // 100 % 10
# num3 = num % 100 // 10
# num4 = num % 10
#
# new_num = f'{num4}{num3}{num2}{num1}'
#
# print(f"{num}反向的数是：{new_num}")

#方法二：
s = str(num)
#使用切片实现反转字符串
s = s[::-1]
print(s)

