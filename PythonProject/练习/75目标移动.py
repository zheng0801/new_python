# 给定一个数组nums和目标值target。将target元素移动到数组前面，其他元素相对顺序不变。

nums = [1, 34, 45, 56, 3, 23, 3, 43, 53, 24, 241, 53, 3, 94]
target = int(input('请输入目标值：'))

# #方法一：
# if target in nums:
#     for i in range(len(nums)):
#         if target == nums[i]:
#             del nums[i]
#             nums.insert(0, target)
#     print(nums)
# else:
#     print('数组中不存在目标值')
#     print(nums)

#方法二：
def func(nums, target):
    count = 0
    left = len(nums) - 1
    right = len(nums) - 1
    while left >= 0:
        if nums[left] != target:
            nums[right] = nums[left]
            right -= 1
        else:
            count += 1
        left -= 1
    for i in range(count):
        nums[i] = target


func(nums,target)
print(nums)



