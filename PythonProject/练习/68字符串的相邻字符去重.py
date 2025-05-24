# 给定一个仅由英文小写字母组成的字符串ss，将相邻且相同的两个字符删掉构成新的字符串，重
# 复删除操作直至生成不符合删除条件的字符串并返回。输入:'acbbc’输出:'a'

ss = input('请输入字符串：')

def func(s):
    new_s = ''
    for i in s:
        if new_s == '':
            new_s += i
        elif new_s[-1] == i:
            new_s = new_s[:-1]
        else:
            new_s += i
    return new_s

print(func(ss))