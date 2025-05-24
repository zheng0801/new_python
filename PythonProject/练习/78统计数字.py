# 给定一个数字k，计算k在0到n中出现的次数

k = input('请输入一个数字：')
n = int(input('请输入一个数字n：'))

def func(k, n):
    count = 0
    for i in range(1, n+1):
        time = str(i).count(str(k))
        count += time
    return count

print(func(k, n))

