# 编写程序，输入两个直角边长，求出三角形斜边的长度。
# 勾股定理:a^2+b^2=C^2
import math

num1 = int(input('请输入第一个直角边长：'))
num2 = int(input('请输入第二个直角边长：'))

#使用sqrt()函数计算平方根
# length = math.sqrt(num1**2 + num2**2)

#使用pow()函数求x的y次方
length = math.pow(num1**2 + num2**2,0.5)

print(f'三角形的斜边长是：{length}')