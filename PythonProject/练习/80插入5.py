# 给定一个数字，在数字的任意位置插入一个5使得插入后的这个数字最大。

num = input('请输入一个数字：')

def func(num):
    int_num= int(num)
    if int_num >= 0:
        for i in range(len(num)):
            if int(num[i]) < 5:
                num = num[:i] + '5' + num[i:]
                return num
        return '5' + num
    else:
        for i in range(1, len(num)):
            if int(num[i]) > 5:
                num = num[:i] + '5' + num[i:]
                return num
        return num+'5'

print(func(num))
