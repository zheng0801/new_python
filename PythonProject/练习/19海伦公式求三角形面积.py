# 海伦公式是利用三角形的三条边的边长直接求三角形面积的公式。
# p=(a+b+c)/2   S=sqrt(p*(p-a)*(p-b)*(p-c))

import math

a = float(input('请输入第一条边长：'))
b = float(input('请输入第二条边长：'))
c = float(input('请输入第三条边长：'))

p = (a + b + c) / 2

S = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(f'三角形的面积是：{S:.2f}')