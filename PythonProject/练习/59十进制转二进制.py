# Python实现十进制转二进制。

num = int(input('请输入要转换成二进制的数：'))

#定义一个函数，用来进行数据进制转换
def change_num(num):
    s = ''
    while True:
        s += str(num % 2)
        num //= 2
        if num == 1:
            s += str(num)
            break
    s = s[::-1]
    return s

print(f'{num}转换成二进制是：{change_num(num)}')