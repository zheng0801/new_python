# 一个数如恰好等于除了它以外的因子之和:这个数就称为“完数”。
# 编程序找出1000以内的所有完数，(6是一个"完数"，它的因子是1,2,3)

for i in range(1, 1000):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(f'{i}是完数')
