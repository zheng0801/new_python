# 创建⼀个列表，其中包含⼀系列简短的⽂本消息。将这个列表传递给⼀个名为 show_messages() 的函数，这个函数会打
# 印列表中的每条⽂本消息。

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages_2):
    while messages_2:
        pop_message = messages_2.pop()
        print(pop_message)
        sent_messages.append(pop_message)

    return sent_messages

messages = ['周一', '周二', '周三', '周四', '周五']
sent_messages = []
messages_2 = messages[:]

# show_messages(messages)

# 在为练习 8.9 编写的程序中，编写⼀个名为send_messages() 的函数，将每条消息都打印出来并移到⼀个名为
# sent_messages 的列表中。调⽤ send_messages() 函数，再将两个列表都打印出来，确认把消息移到了正确的列表中。

# send_messages(messages)
# print(send_messages(messages))

# 修改为练习 8.10 编写的程序，在调⽤函数send_messages() 时，向它传递消息列表的副本。调⽤
# send_messages() 函数后，将两个列表都打印出来，确认原始列表保留了所有的消息。
print(messages)
send_messages(messages_2)
print(sent_messages)
print(messages_2)