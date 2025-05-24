# python实现插入排序

nums = [3, 31, 22, 30, 5, 8, 16, 23, 56, 49]

# #方法一：
# #循环进行插入排序，需要从第二个数开始执行len(nums)-1次
# for i in range(1, len(nums)):
#     #已经进行过排序的新的序列
#     new_nums = nums[0:i]
#     #将i索引的值和已经排序过的序列在对比并插入
#     for j in range(len(new_nums)):
#         #当值小于序列中的某个值时，在该位置插入该值，并删除原有索引位置加一上的值
#         if nums[i] < new_nums[j]:
#             nums.insert(j,nums[i])
#             del nums[i+1]
#             # print(nums)
#
# print(nums)

#方法二：
#定义一个排序函数
def insert_sort(li):
    for i in range(1, len(li)):
        j = i - 1
        #拿出要比对的值
        key = li[i]
        while j >= 0:
            if li[j] > key:
                li[j+1] = li[j]
                li[j] = key
            j -= 1
    return li

print(insert_sort(nums))