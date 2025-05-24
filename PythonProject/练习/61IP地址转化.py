# IP地址是一个用'.'隔开的四段数字，请你把IP地址转换成一个整数(IPv4)。
# 例如，114.55.207.244 的二进制表示是 01110010 00110111 11001111 11110100，其十进制表示是1916260340.

ip = input('请输入ip地址：')
list_ip = ip.split('.')
new_list_ip = []

# #方法一：
# def change_num(num):
#     s = ''
#     while True:
#         s += str(num % 2)
#         num //= 2
#         if num == 1:
#             s += str(num)
#             break
#     while len(s) < 8:
#         s += '0'
#     s = s[::-1]
#     return s
#
# for i in list_ip:
#    new_list_ip.append(change_num(int(i)))
#
# print(new_list_ip)
#
# for i in new_list_ip:
#     print(i, end=' ')

#方法二：
def func(str):
    strs = str.split('.')
    res = ''
    for i in strs:
        res += '{:08b}'.format(int(i))
    return int(res, 2)

print(func(ip))
