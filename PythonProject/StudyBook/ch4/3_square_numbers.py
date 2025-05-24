# 如何创建⼀个列表，其中包含前 10 个整数（1〜10）的平方

square_number = []

for number in range(1,11):
    square_number.append(number ** 2)
print(square_number)