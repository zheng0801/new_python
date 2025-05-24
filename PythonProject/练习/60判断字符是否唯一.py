# 给定一个字符串，请你判断其中每个字符是否全都不同。

s = input('请输入字符串：')
flag = True

#判断字符在字符串是否存在多次，存在多次返回False
for i in range(len(s)):
    new_s = s
    new_s = new_s.replace(s[i], '', 1)
    if s[i] in new_s:
        flag = False
        break

if flag:
    print('该字符串中每个字符全部不同')
else:
    print('该字符串中存在相同字符')