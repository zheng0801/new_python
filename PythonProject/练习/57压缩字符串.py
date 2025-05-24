# 利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
# 比如，字符串aabcccccaaa会变为a2bc5a3。
# 1.如果只有一个字符，1不用写
# 2.字符串中只包含大小写英文字母(a至z)

import re

s = input('请输入字符串（只能输入英文字母）：')
new_s = []

#确保输入的字符串只包含大小写英文字母
for i in s:
    if re.match(r'[^a-zA-Z]$', i):
        s = input('输入的字符串中包含非英文字母，请重新输入：')
        break

#定义一个函数用来实现压缩功能
def frequency(s):
    #空字符串直接返回
    if not s:
        return s
    char = s[0]
    sum = 1
    #将char和之后的每个字符串对比
    for i in s[1:]:
        #如果相等，总数加一
        if i == char:
            sum += 1
        else:
            #不相等直接将改字符串加入列表，如果总数大于1，将总数加入列表，并将验证过的值赋给char重置sum
            new_s.append(char)
            if sum > 1:
                new_s.append(str(sum))
            char = i
            sum = 1
    #以上循环会不对最后一位数，或最后几位数相等的数做处理
    #直接添加最后一位数到列表，并判断总数
    new_s.append(char)
    if sum > 1:
        new_s.append(str(sum))
    #拼接列表值
    return ''.join(new_s)

print(frequency(s))


