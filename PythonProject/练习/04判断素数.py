# 编写程序，判断某一个数是否为素数。
# 所谓素数指的是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数。

num = int(input('请输入一个数：'))

# i = 2
# number = True
# while(i < num):
#     if num % i == 0:
#         number = False
#         break
#     else:
#         i += 1
#
# if number:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')


flag = True
for i in range(2, num):
    #
    if num % i == 0:
        flag = False
        break

if flag:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')
