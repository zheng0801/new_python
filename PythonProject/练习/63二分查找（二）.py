# 请实现有重复数字的升序数组的二分查找
# 给定一个元素有序的(升序)长度为n的整型数组 nums 和一个目标值 target ，
# 写一个函数搜索nums中的第一个出现的target,如果目标值存在返回下标，否则返回 -1。

nums = [1, 3, 3, 6, 7, 11, 32, 32, 55, 99, 99, 99, 101, 120, 139]

target = int(input('请输入您要查找的数字：'))

#定义一个函数二分查找
def func(nums, target):
    result = -1
    left = 0
    right = len(nums) - 1
    #当左右指标未交叉时循环
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            result = middle
            #将右指标的值赋为中间值减一，验证查到的目标值时最早出现的
            right = middle - 1
        elif nums[middle] > target:
            right = middle - 1
        elif nums[middle] < target:
            left = middle + 1
    return result

print(func(nums, target))