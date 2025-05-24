# 按照下⾯的说明编写⼀个程序，模拟⽹站如何确保每个⽤户的⽤户名都独⼀⽆⼆。
# 创建⼀个⾄少包含 5 个⽤户名的列表，并将其命名为current_users。
# 再创建⼀个包含 5 个⽤户名的列表，将其命名为 new_users，并确保其中有⼀两个⽤户名也在列表 current_users 中。
# 遍历列表 new_users，检查其中的每个⽤户名是否已被使⽤。如果是，就打印⼀条消息，指出需要输⼊别的⽤户名；否则，打印⼀条消息，
# 指出这个⽤户名未被使⽤。
# 确保⽐较时不区分⼤⼩写。换句话说，如果⽤户名 'John' 已被使⽤，应拒绝⽤户名 'JOHN'。（为此，需要创建列表
# current_users 的副本，其中包含当前所有⽤户名的全⼩写版本。）

current_users = ['zheng','Lin','wang','chen','jiang']
new_users = ['zheng','deng','ye','lin','sun']
current_users_2 = []

for current_user in current_users:
    current_users_2.append(current_user.lower())

print(current_users_2)

for new_user in new_users:
    if new_user.lower() in current_users_2:
        print(f'{new_user}用户名已存在，请重新命名')
    else:
        print(f'{new_user}该用户名未被使用，创建成功')
