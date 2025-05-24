# 有一分数序列:2/1，3/2，5/3，8/5，13/8，21/13.求出这个数列的前20项之和

n = 2
m = 1
count = 0

for i in range(20):
    count += n / m
    k = n
    n = n + m
    m = k

print(count)