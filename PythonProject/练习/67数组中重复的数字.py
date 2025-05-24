# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出是2或者3。存在不合法的输入的话输出-1。


n = input('请输入一个数据（用空格隔开）：')
nums = n.split(' ')

# #方法一：
# #定义一个函数判断是否重复
# def func(nums):
#     result = -2
#     # 判断列表内的数据时候都小于n
#     for i in nums:
#         if int(i) >= len(nums) or int(i) < 0:
#             result = -1
#     #判断是否存在重复数字
#     for i in range(len(nums)):
#         new_nums = nums[:]
#         del new_nums[i]
#         if nums[i] in new_nums:
#             result = nums[i]
#             break
#     return result
#
# if int(func(nums)) >= -1:
#     print(func(nums))


#方法二：
def func(nums):
    for i in nums:
        if nums.count(i) > 1:
            return i
    return -1

print(func(nums))


