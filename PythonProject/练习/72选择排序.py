# python实现选择排序

nums = [3, 31, 22, 30, 5, 8, 16, 23, 56, 49]

for i in range(len(nums)-1):
    big_num = nums[i+1]
    for j in range(i, len(nums)):
        #找出最大值所在索引，然后将最大值和循环轮次所属索引的值互换
        if nums[j] > big_num:
            result = j
            big_num = nums[j]

    nums[i], nums[result] = nums[result], nums[i]

print(nums)
