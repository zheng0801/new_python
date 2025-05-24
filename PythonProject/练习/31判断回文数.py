# 输入一个数，判断它是不是回文数。12321是回文数，个位与万位相同，十位与千位相同。

num = input('请输入一个数：')

# # 方法一：
# length = len(num)
#
# for i in range(length//2):
#     flag = True
#     if num[i] != num[-(i+1)]:
#         flag = False
#         break
#
# if flag:
#     print('您输入的数是回文数')
# else:
#     print('您输入的数不是回文数')

#方法二：使用切片翻转数据
num2 = num[::-1]

if num2 == num:
    print('您输入的数是回文数')
else:
    print('您输入的数不是回文数')