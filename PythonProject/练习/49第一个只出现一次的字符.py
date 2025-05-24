# 在一个字符串中找到第一个只出现一次的字符,并返回它的位置,如果没有则返回 -1(需要区分大小写).(从O开始计数)

s = input('请输入字符串：')
flag = -1


# #方法一
# #定义一个函数，用来查找字符串中的某个字符出现的次数
# def find_str(s, x):
#     sum = 0
#     for i in s:
#         if i == x:
#             sum += 1
#     return sum
#
# #统计字符串中的每个字母出现次数，当出现一个次数为1的字母时结束循环，并修改flag值
# for i in s:
#     if find_str(s, i) == 1:
#         print(s.find(i))
#         flag = 1
#         break
#
# #当flag为1说明不存在只出现一次的字母，打印-1
# if flag == -1:
#     print(flag)

#方法二：
#创建一个空字典
mp = dict()

#循环将字符串每个字符放到字典中，并将该字符出现次数设为值
for i in s:
    if i in mp:#如果该字符已存在key，则value+1
        mp[i] += 1
    else:
        mp[i] = 1

#循环查找字符串中字符出现次数，为1时结束循环，将索引赋予flag
for i in range(len(s)):
    if mp[s[i]] == 1:
        flag = i
        break

print(flag)


