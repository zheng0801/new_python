# 输入某年某月某日，判断这一天是这一年的第几天。
import datetime


# #方法一
# time = input('请输入年月日：')
#
# year = int(time[0:4])
# month = int(time[4:6])
# day = int(time[6:])
#
# sum_day = day
# print(f'{sum_day}a')
#
# for i in range(1, month):
#     if i % 2 == 0:
#         sum_day += 30
#         print(f'{sum_day}b')
#     elif i % 2 != 0:
#         sum_day += 31
#         print(f'{sum_day}c')
#
# if month > 2:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         sum_day = sum_day - 1
#         print(f'{sum_day}d')
#     else:
#         sum_day = sum_day - 2
#         print(f'{sum_day}e')
#
# print(f'{time}是{year}这年的第{sum_day}天')


#方法二
year, mouth, day = map(int, input('请输入年月日，用空格隔开：').split(' '))

new_year_days = datetime.datetime(year, 1, 1)
now = datetime.datetime(year,mouth,day)

sum_days = (now-new_year_days).days + 1
print(sum_days)

# now = datetime.datetime.now()
# print(now.second)
# day1 = datetime.datetime(2025, 1, 1)
# print((now - day1).days)


