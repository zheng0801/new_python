# 编写程序，输入整数a、b表示一个闭区间找出该区间内的所有素数并打印
# 所谓素数指的是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。

a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
list = []

# #方法一
# for i in range(a, b+1):
#     flag = True
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#
#     if flag:
#         list.append(i)

#方法二
#定义一个函数用来判断某个数是不是素数，返回False表示不是素数
def prime(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    return flag

#在区间内循环调用prime()判断是否是素数
for i in range(a, b+1):
    if prime(i):
        list.append(i)


print(f'在{a}到{b}区间之间的素数有：{list}')