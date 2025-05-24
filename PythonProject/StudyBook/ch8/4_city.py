# 编写⼀个名为 describe_city() 的函数，它接受⼀座城市的名字以及该城市所属的国家。这个函数应该打印⼀个像下
# ⾯这样简单的句⼦。Reykjavik is in Iceland.
# 给⽤于存储国家的形参指定默认值。为三座不同的城市调⽤这个函数，其中⾄少有⼀座城市不属于默认的国家。

def describe_city(name = 'changsha', country = 'china'):
    print(f'{name.title()} is in {country.title()}')

describe_city()
describe_city(name = 'beijing')
describe_city(name = 'reykjavik', country = 'iceland')