# 在提⽰⽤户提供数值输⼊时，常出现的⼀个问题是，⽤户提供的是⽂本⽽不是数。在这种情况下，当你尝试将输⼊
# 转换为整数时，将引发 ValueError 异常。编写⼀个程序，提⽰⽤户输⼊两个数，再将它们相加并打印结果。在⽤户输⼊的任意⼀个值不
# 是数时都捕获 ValueError 异常，并打印⼀条友好的错误消息。对你编写的程序进⾏测试：先输⼊两个数，再输⼊⼀些⽂本⽽不是数。
# 将为练习 10.6 编写的代码放在⼀个 while 循环中，让⽤户在犯错（输⼊的是⽂本⽽不是数）后能够继续输⼊数。

# number_one = input('请输入第一个数：')
# number_two = input('请输入第二个数：')
#
#
# try:
#     answer = int(number_one) + int(number_two)
# except ValueError:
#     print('请输入数字！!')
# else:
#     print(answer)

action = True
while action:
    number_one = input('请输入第一个数：')
    number_two = input('请输入第二个数：')

    try:
        answer = int(number_one) + int(number_two)
    except ValueError:
        print('请输入数字！!')
    else:
        print(answer)

    number = input('是否继续执行，结束请输入q！: ')

    if number == 'q':
        action = False


