# 球从100米高度自由落下，每次落地后反跳回原高度的一半;再落下，求它在第10次落地时，共经过多少米?第10次反弹多高?

height = 100

# 方法一：
sum = 0

for i in range(1, 11):
    if i == 1:
        sum  = sum + height
    else:
        sum = sum + height
    height = height / 2

print(f'共经过{sum}米，第十次反弹了{height*2}米')

# #方法二：
# count = 0
# list = []
#
# while count < 10:
#     if count == 0:
#         list.append(height)
#         height /= 2
#         count += 1
#     else:
#         list.append(height*2)
#         height /= 2
#         count +=1
#
# print(f'共经过了：{sum(list)}米，第十次反弹了{height*2}米。')

