# 输入字符串，求其长度。

s = input('请输入内容：')

# #方法一：
# print(len(s))

#方法二：
length = 0

for i in s:
    length += 1

print(length)