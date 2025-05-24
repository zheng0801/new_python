# 将同⼀个数乘三次称为⽴⽅。例如，在 Python 中，2的⽴⽅⽤ 2**3 表⽰。创建⼀个列表，其中包含前 10 个整数（1〜
# 10）的⽴⽅，再使⽤⼀个 for 循环将这些⽴⽅数打印出来。

# numbers =[]
# for number in range(1,11):
#     numbers.append(number ** 3)

numbers = list(number ** 3 for number in range(1,11))#对应的立方推导式

for number in numbers:
    print(number)
