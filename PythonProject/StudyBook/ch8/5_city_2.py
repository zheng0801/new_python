# 编写⼀个名为 city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回⼀个格式类似于下⾯的
# 字符串："Santiago, Chile"
# ⾄少使⽤三个城市⾄国家对调⽤这个函数，并打印它返回的值。

def city_country(name, country):
    message = f'{name.title()}, {country.title()}'
    return message

print(city_country('santiago', 'chile'))
print(city_country(name = 'changsha', country = 'china'))
print(city_country(country = 'china', name = 'beijing'))