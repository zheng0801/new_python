# 创建⼀个名为 cities 的字典，将三个城市名⽤作键。对于每座城市，都创建⼀个字典，并在其中包含该城市所属的国
# 家、⼈⼝约数以及⼀个有关该城市的事实。表⽰每座城市的字典都应包含 country、population 和 fact 等键。将每座城市的名字以及
# 相关信息都打印出来。

cities = {
    'fuzhou': {
        'nation': 'china',
        'population': 12000000,
        'fact': '福州是福建的省会',
    },
    'xiemen': {
        'nation': 'china',
        'population': 7000000,
        'fact': '厦门是经济特区',
    },
    'quanzhou': {
        'nation': 'china',
        'population': 8000000,
        'fact': '具有悠久的历史',
    },
}

for city, messages in cities.items():
    print(f'这个城市是：{city.title()}')

    print(f"所属国家是：{messages['nation']}\t人口约数：{messages['population']}\t一个冷知识：{messages['fact']}")

    # i = 0
    # for message1, message2 in messages.items():
    #     if i == 0:
    #         print(f'所属的国家是：{message2}')
    #     elif i == 1:
    #         print (f'人口约数：{message2}')
    #     elif i ==2:
    #         print(f'一个冷知识：{message2}')
    #     i += 1

    # for message1, message2 in messages.items():
    #     print(f'{message1}：{message2}')