# 给定两个字符串，判断其中一个字符串是否为另个字符串的置换。
# 置换的意思是，通过改变顺序可以使得两个字符串相等。

string_one = input('请输入第一个字符串：')
string_two = input('请输入第二个字符串：')

A = sorted(string_one)
B = sorted(string_two)

if A == B:
    print(f'{string_one}是{string_two}的置换')
else:
    print(f'{string_one}不是{string_two}的置换')