# 创建⼀个包含数 1〜1 000 000 的列表，再使⽤⼀个for 循环将这些数打印出来。（如果输出的时间太⻓，按 Ctrl + C 停⽌
# 输出，或关闭输出窗⼝。）

number_list = list(range(1,1_000_001))#创建1-1000000的列表
#
# for number in number_list:#打印列表
#     print(number)

# 创建⼀个包含数 1〜1 000 000 的列表，再使⽤min() 和 max() 核实该列表确实是从 1 开始、到 1 000 000 结束的。
# 另外，对这个列表调⽤函数 sum()，看看 Python 将 100 万个数相加需要多⻓时间。

print(min(number_list))
print(max(number_list))
print(sum(number_list))