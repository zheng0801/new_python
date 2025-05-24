# 编写⼀个名为 make_album() 的函数，它创建⼀个描述⾳乐专辑的字典。这个函数应接受歌⼿名和专辑名，并返回⼀个
# 包含这两项信息的字典。使⽤这个函数创建三个表⽰不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给 make_album() 函数添加⼀个默认值为 None 的可选形参，以便存储专辑包含的歌曲数。如果调⽤这个函数时指定了歌曲数，就将这个
# 值添加到表⽰专辑的字典中。调⽤这个函数，并⾄少在⼀次调⽤中指定专辑包含的歌曲数。

def make_album(singer_name, album_name,sing_number=None):

    albums = {'name': singer_name, 'album': album_name}
    if sing_number:
        albums['singer_number'] = sing_number
    return albums
#
# print(make_album('张杰', '逆战'))
# print(make_album(album_name = '我的骄傲', singer_name = '容祖儿'))
# print(make_album(singer_name ='不爱之恩', album_name = 'Twins'))
# print(make_album('讨好自己', '王菲', 5))

# 在为练习 8.7 编写的程序中，编写⼀个 while循环，让⽤户输⼊歌⼿名和专辑名。获取这些信息后，使⽤它们来调
# ⽤ make_album() 函数并将创建的字典打印出来。在这个 while 循环中，务必提供退出途径。

action = True

while action:
    print('请再下面输入您喜欢的歌手名和专辑名，可在任意环节以q结束')
    name = input('请输入歌手名：')
    if name == 'q':
        break
    album = input('请输入专辑名：')
    if album == 'q':
        break
    number = input('请输入专辑收藏歌数：')
    if number == 'q':
        break
    albums_2 = make_album(singer_name=name, album_name=album, sing_number=number)
    print(albums_2)

    repeat = input('是否继续执行（yes/no）：')
    if repeat == 'no':
        action = False