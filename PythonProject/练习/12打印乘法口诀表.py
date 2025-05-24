#编写程序打印乘法口诀表

# #方法一
# for i in range(1, 10):
#     list = []
#     for j in range(1, i+1):
#         list.append(f'{i} * {j} = {i*j} ')
#     #将列表内容转换成字符串，并用看空格隔开，只适用于列表元素全是字符串类型，如包含非字符串类型的则需先进行类型转换
#     result = ' '.join(list)
#     print(result)

#方法二

for i in range(1, 10):
    print('\n')
    for j in range(1, i+1):
        #打印并以空格做多个对象间的分隔符
        print(f'\t{i}*{j}={i*j}', end=' ')