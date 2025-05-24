# 创建⼀个列表，其中包含 3〜30 内能被 3 整除的数，再使⽤⼀个 for 循环将这个列表中的数打印出来。

numbers = []
for number in range(3,31):
    if number % 3 == 0:
        numbers.append(number)

for number in numbers:
    print(number)