# 修改为练习 6.2 编写的程序，让每个⼈都可以有多个喜欢的数字，然后将每个⼈的名字及其喜欢的数打印出来。

numbers = {
    'joe': [20, 4],
    'jelly': [88],
    'sky': [88, 99, 66],
    'jimmy': [0, 10, 19],
    'tony': [999],
}

for name, number in numbers.items():
    if len(number) == 1:
        print(f'{name}喜欢的数字有：{number}')
    else:
        print(f'{name}喜欢的数字有：')
        for i in number:
            print(f'\t{i}')
#  name = input('请输入名字：')
#
#  for key, value in numbers.items():
#      if name in key:
#          print(value)


