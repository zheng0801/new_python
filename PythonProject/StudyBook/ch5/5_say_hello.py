# 创建⼀个⾄少包含 5 个⽤户名的列表，并且其中⼀个⽤户名为 'admin'。想象你要编写代码，在每
# 个⽤户登录⽹站后都打印⼀条问候消息。遍历⽤户名列表，向每个⽤户打印⼀条问候消息。
# 如果⽤户名为 'admin'，就打印⼀条特殊的问候消息，如下所⽰。
# Hello admin, would you like to see a status report?
# 否则，打印⼀条普通的问候消息，如下所⽰。
# Hello Jaden, thank you for logging in again.

users =['admin','zheng','lin','chen','wang']
#
# for user in users:
#     if user == 'admin':
#         print(f'Hello {user}, would you like to see a status report?')
#     else:
#         print(f'Hello {user}, thank you for logging in again.')

# 在为练习 5.8 编写的程序中，添加⼀条 if 语句，检查⽤户名列表是否为空。
# 如果为空，就打印如下消息。
# We need to find some users!
# 删除列表中的所有⽤户名，确认将打印正确的消息。

for i in range(0,len(users)):#循环删除列表中索引0-(len(users)-1)的元素
    del users[0]

print(users)
if users:
    print('We need to find some users!')
else:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')

