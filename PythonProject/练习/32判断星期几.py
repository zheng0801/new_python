# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 星期一 Monday、星期二 Tuesday、星期三Wednesday、星期四 Thursday、星期五 Friday 、星期六 Saturday、星期日Sunday。

#方法一；使用字典
letter = input('输入星期第一个字母：').upper()

weeks = {
    'Monday': '星期一',
    'Tuesday': '星期二',
    'Wednesday': '星期三',
    'Thursday': '星期四',
    'Friday': '星期五',
    'Saturday': '星期六',
    'Sunday': '星期日'
}

#创建一个空字典，存放查询首字母后的结果
new_weeks ={}

#循环查出首字母和查询条件一致的星期
for week in weeks.keys():
    if letter == week[0]:
        new_weeks[week] = weeks[week]

#如果查询结果有多个，则让用户输入第二个字母，并从新的字典中查询第二字母符合的星期
if len(new_weeks) > 1:
    letter_two = input('请输入星期第二个字母：').lower()
    for week in new_weeks.keys():
        if letter_two == week[1]:
            print(new_weeks[week])
    if new_weeks[week]:
        print('第二字母输入有误')
elif len(new_weeks) == 1:
    print(new_weeks.values())
elif len(new_weeks) == 0:
    print('首字母输入有误')

# #方法二：
# a = input('请输入第一个字母：').upper()
#
# if a == 'M':
#     print('星期一')
# elif a =='W':
#     print('星期三')
# elif a == 'F':
#     print('星期五')
# elif a == 'T' or a == 'S':
#     b = input('请输入第二个字母').lower()
#     if a =='T':
#         if b == 'u':
#             print('星期二')
#         elif b == 'h':
#             print('星期四')
#         else:
#             print('第二字母输入有误')
#     if a == 'S':
#         if b == 'a':
#             print('星期六')
#         elif b == 'u':
#             print('星期日')
#         else:
#             print('第二字母输入有误')
# else:
#     print('首字母输入有误')

