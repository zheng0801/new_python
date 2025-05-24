# 编写程序，输入半径，求出圆的面积。
# 圆的面积=π*r*r

import math

r = float(input('请输入圆的半径：'))

area = math.pi * r**2

print(f"{area:.2f}")
