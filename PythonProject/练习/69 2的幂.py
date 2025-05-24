# 给定一个非负整数n，请问是否存在一个x满足2^x=n，如果有，则返回true，否则返回false

import math

n = int(input('请输入一个非负整数：'))

x = math.log2(n)
if x.is_integer():
    print(True)
else:
    print(False)