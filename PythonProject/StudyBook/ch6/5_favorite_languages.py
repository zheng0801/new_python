# 在 6.3.1 节编写的程序 favorite_languages.py 中执⾏以下操作。
# 创建⼀个应该会接受调查的⼈的名单，其中有些⼈已在字典中，⽽其他⼈不在字典中。
# 遍历这个名单。对于已参与调查的⼈，打印⼀条消息表⽰感谢；
# 对于还未参与调查的⼈，打印⼀条邀请参加调查的消息。

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, favorite_language in favorite_languages.items():
    print(f'{name.title()}\'s favorite language is {favorite_language.title()}')

lists = ['jen', 'sarah', 'sky', 'joe', 'jimmy']

for name in lists:
    if name.lower() in favorite_languages.keys():
        print('感谢您参与调查')
    else:
        print('您还未参加该调查，如果您有空的话随时欢迎参加此次调查')
