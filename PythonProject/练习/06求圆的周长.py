# 编写程序，输入半径，求出圆的周长
# 圆的周长=2πr=πd
import math
#导入数学模块

r = float(input('请输入圆的半径：'))

# perimeter = 2 * r * 3.14159

#通过数学模块中的pi函数
perimeter = 2 * math.pi * r

#通过:.2f来规定输出小数后两位
print(f'{perimeter:.2f}')