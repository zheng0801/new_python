# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input('请输入一串字符：')
english_num, num, order_num ,space = 0, 0, 0, 0

for i in s:
    if i.isalpha():#判断是否是字母
        english_num += 1
    elif i.isspace():#判断是否是空格
        space += 1
    elif i.isdigit():#判断是否是数字
        num += 1
    else:
        order_num += 1

print(f'输入的字符串中包括英文字母空格：{english_num}个，空格：{space}个,数字：{num}个，其他字符：{order_num}个')