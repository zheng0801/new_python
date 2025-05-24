# 给定两个字符串S和T，判断S是否是T的子序列。即是否可以从T删除一些字符转换成S

s = input('请输入第一个字符串：')
t = input('请输入第二个字符串：')

#定义一个函数判断是否是子序列，是返回True，否返回False
def func(a, b):
    #如果a长度大于b返回False
    if len(a) >= len(b):
        return False
    else:
        sum = 0
        new_s = ''
        for i in b:
            if i == a[sum]:
                new_s = new_s + i
                sum += 1
        if new_s == a:
            return True

if func(s, t):
    print(f'{s}是{t}的子序列')
else:
    print(f'{s}不是{t}的子序列')