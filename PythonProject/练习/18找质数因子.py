# 输入一个正整数，输出它的所有质数因子(如180的质数因子为2、2、3、3、5)。

num = int(input('请输入一个正整数：'))
a = 2
list = []

#循环算出所有的质因子
while num != a:
    if num % a == 0:
        list.append(a)
        num /= a
    else:
        a += 1
list.append(a)


print(f'质数因子有：', end=' ')
for i in list:
    print(f'{i}', end=',')