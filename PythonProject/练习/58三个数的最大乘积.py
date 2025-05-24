# 给定一个长度为n的无序数组，包含正数、负数和0，请从中找出3个数，使得乘积最大，返回这个乘积。

n = input('请输入数字（数字用空格隔开）：')
new_list = []


#将字符串用分割存储到列表中
list_l = n.split(' ')

#循环转换列表中数据类型
for i in list_l:
    new_list.append(int(i))

#对列表进行排序
new_list.sort()

list_one = new_list
count = 0
#将任意三个数相乘比较大小留下大的乘积
#第一次循环得到第一个数
for i in range(len(list_one)):
    list_two = list_one[:]
    #将原列表去掉第一个数
    del list_two[i]
    #第二次循环得到第二个数
    for j in range(len(list_two)):
        list_three = list_two[:]
        #去掉第二个数生成新列表
        del list_three[j]
        #第三次循环在新的列表中循环拿到第三个数
        for k in range(len(list_three)):
            #计算三个数的乘积
            sum = new_list[i] * list_one[j] * list_three[k]
            #如果是第一个数，则直接返回乘积
            if i == 1 and j == 1 and k == 1:
                count = sum
                print(count)
            elif sum > count:
                count = sum
                print(count)
    #将原列表重置
    list_one = new_list[:]

print(f'该数字三位数最大乘积是：{count}')