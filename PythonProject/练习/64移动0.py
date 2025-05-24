# 给定一个数组，请你实现将所有0移动到数组末尾并且不改变其他数字的相对顺序。

nums = [1, 4, 0, 5, 3, 0, 54, 23, 4, 0, 43]
sum = 0
new_nums = []

# #方法一：
# #循环统计0出现次数，将非0数加到新列表中
# for i in range(len(nums)):
#     if nums[i] == 0:
#         sum += 1
#     else:
#         new_nums.append(nums[i])
#
# #将统计的0加到新列表末尾
# if sum > 0:
#     for i in range(sum):
#         new_nums.append(0)
#
# print(new_nums)

#方法二：
def func(nums):
    for i in nums:
        #如果该数等于0，直接从列表中删除，并在末尾添加一个0
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums

print(func(nums))