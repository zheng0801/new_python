# 给定两个字符串str和sub，从str中完全删除在sub中存在的字符。

str = input('请输入字符串：')
sub = input('请输入要删除的字符串：')

# #方法一：
# for i in sub:
#     for j in str:
#         if i == j:
#             str = str.replace(j, '')
#
# print(str)

#方法二：
def func(str, sub):
    #将要删除的字符加入到集合中，集合中自动去重
    s = set(sub)
    ans = ''
    for c in str:
        if c not in s:
            ans += c
    return ans

print(func(str, sub))