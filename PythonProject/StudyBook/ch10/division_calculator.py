
print('Give me two numbers, and I\'ll divide them.')
print('Enter \'q\' to quit.')

# try:
#     while True:
#         '''循环进行除法运算'''
#         first_number = input('\nFirst number: ')
#         if first_number == 'q':
#             break
#         second_number = input('Second number: ')
#         if second_number == 'q':
#             break
#         answer = int(first_number) / int(second_number)
#         print(answer)
# except ZeroDivisionError:#报ZeroDivisionError输出提示
#     print('You can\'t divide by zero!')


while True:
    '''循环进行除法运算'''
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:  # 报ZeroDivisionError输出提示
        print('You can\'t divide by zero!')
    else:
        print(answer)

