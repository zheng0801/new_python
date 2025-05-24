# 求一个3*3矩阵主对角线元素之和

#方法一：
#确定要求的矩阵阶数
n = int(input('请问你要求n阶矩阵：'))
sum = 0
list = []

#循环添加矩阵的数据
for i in range(n):
    list.append([])
    for j in range(n):
        num = int(input(f'a{i+1}{j+1}的值是：'))
        list[i].append(num)
        #计算主对角线的值之和
        if i == j:
            sum += list[i][j]

print(sum)


# #方法二：
# a = []
# sum = 0
#
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         k = int(input('请输入数据：'))
#         a[i].append(k)
#         if i == j:
#             sum += a[i][j]
#
# print(a)
# print(sum)