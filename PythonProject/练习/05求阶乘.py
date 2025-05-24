# 编写程序，求出某个自然数的阶乘。
# 一个正整数的阶乘是所有小于及等于该数的正整数的积，并且0的阶乘为1。自然数n的阶乘写作n!

# 方法一：非递归
num = int(input('请输入一个数：'))
# result = 1
# if num == 0:
#     result = 1
# else:
#     for i in range(1,num+1):
#         result = result * i
#
# print(f'{num}的阶乘是：{result}')

#方法二：递归
def factorial(num):
    if num == 1 or num == 0:
        return 1
    # elif num == 0:
    #     return 1
    else:
        return num * factorial(num - 1)

print(f'{num}的阶乘是：{factorial(num)}')
