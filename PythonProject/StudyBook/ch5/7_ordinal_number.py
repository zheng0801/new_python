# 序数表⽰顺序位置，如 1st 和 2nd。序数⼤多以 th 结尾，只有 1st、2nd、3rd 例外。
# 在⼀个列表中存储数字 1〜9。
# 遍历这个列表。
# 在循环中使⽤⼀个 if-elif-else 结构，打印每个数字对应的序数。输出内容应为 "1st 2nd 3rd 4th 5th 6th 7th 8th
# 9th"，每个序数都独占⼀⾏。

number_lists = list(range(1,10))

for number in number_lists:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')