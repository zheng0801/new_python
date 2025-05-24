# python实现冒泡排序

nums = [5, 7, 3, 11, 34, 22, 98, 43, 35]

#循环n次，每次都找出最大的值
for i in range(len(nums)):
    for j in range(len(nums)-1-i):
        #比较相邻两个值中的大的值，并将大的值放在索引靠后的位置
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print(nums)