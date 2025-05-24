# 给定两个字符串str1和str2,输出两个字符串的最长公共子串，保证str1和str2的最长公共子串存在且唯一。

str1 = input('请输入第一个字符串：')
str2 = input('请输入第二个字符串：')

def func(str1, str2):
    res = ''
    left = 0
    #循环得出最长公共子串
    for i in range(len(str1)+1):
        if str1[left:i+1] in str2:
            res = str1[left:i+1]
        else:
            left += 1
    return res

print(func(str1, str2))