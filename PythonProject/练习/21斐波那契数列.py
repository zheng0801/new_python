# 又称兔子数列，指的是这样一个数列:1、1、2、3、5、8、13、21、34、..编写程序找出第n个项。

n = int(input('请输入您想查询的项数：'))

# #方法一：
# sum = 1
# x = 0
# y = 1
#
# for i in range(2, n+1):
#     sum = x + y
#     x = y
#     y = sum
#
# print(f'第{n}个项的数是：{sum}')

# #方法二：递归
# #定义斐波那契函数
# def fob(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fob(n-1) + fob(n-2)
#
# print(f"第{n}个项的数是：{fob(n)}")

#方法三：
fobs = [1, 1]

for i in range(2, n+1):
    fobs.append(fobs[i-1] + fobs[i-2])

print(fobs[n-1])

