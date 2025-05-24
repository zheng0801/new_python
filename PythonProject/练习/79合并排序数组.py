# 将有序数组A和B合并，要求合并后的新数组也要有序。

list1 = [1, 4, 7, 8, 9, 11, 15, 18, 23, 45, 53]
list2 = [3, 5, 8, 11, 24, 34, 56, 64, 69, 70, 98]
list = []
i, j = 0, 0

while i < len(list1) and j < len(list2):
    if list1[i] >= list2[j]:
        list.append(list2[j])
        j += 1
    elif list1[i] < list2[j]:
        list.append(list1[i])
        i += 1

if i < len(list1):
    for a in list1[i:]:
        list.append(a)
elif j < len(list2):
    for a in list2[j:]:
        list.append(a)

print(list)










    
