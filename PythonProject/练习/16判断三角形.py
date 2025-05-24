# 编写程序，输入三组数据，判断能否构成三角形的三条边。

print('请输入三组数据：')
list = []

#循环输入数据
for i in range(3):
    num = input()
    list.append(num)

a = int(list[0])
b = int(list[1])
c = int(list[2])

if ( a + b ) > c and ( a + c ) > b and ( b + c ) > a:
    print(f'输入的三组数据构成三角形')
else:
    print('输入的数据构不成三角形')