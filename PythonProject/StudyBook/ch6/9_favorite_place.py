# 创建⼀个名为 favorite_places 的字典。
# 在这个字典中，将三个⼈的名字⽤作键，并存储每个⼈喜欢的 1〜3 个地⽅。为让这个练习更有趣些，让⼀些朋友说出他们喜欢的⼏个地
# ⽅。遍历这个字典，并将其中每个⼈的名字及其喜欢的地⽅打印出来。

favorite_places = {
    'Zheng': ['changsha', 'chongqing', 'chengdu'],
    'Lin': ['beijing'],
    'Chen': ['sanya', 'puer'],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f'{name}喜欢的地方有：{places[0].title()}')
    else:
        print(f'{name}喜欢的地方有：')
        for place in places:
            print(f'\t{place.title()}')