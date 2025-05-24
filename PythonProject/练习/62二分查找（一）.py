# 请实现无重复数字的升序数组的二分查找
# 给定一个 元素升序的、无重复数字的整型数组nums 和一个日标值 target，写一个函数搜索nums 中的 target，
# 如果目标值存在返回下标(下标从0开始)，否则返回-1

nums = [2, 5, 7, 12, 15, 34, 55, 67, 76, 98, 124]

target = int(input('请输入您要查询的数：'))

#定义一个函数进行二分查找
def func(nums, target):
    #令左指标为0，右指标为最后一个索引
    left = 0
    right = len(nums) -1
    #当左右指标为交叉时循环
    while left <= right:
        #算出中间数
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle -1
        elif nums[middle] < target:
            left = middle + 1
    return -1

print(func(nums, target))