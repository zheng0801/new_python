# 编写⼀个函数，它接受两个形参：⼀个城市名和⼀个国家名。这个函数返回⼀个格式为 City, Country 的字符
# 串，如 Santiago, Chile。将这个函数存储在⼀个名为city_functions.py 的模块中，并将这个⽂件存储在⼀个新的⽂件夹中，
# 以免 pytest 在运⾏时，尝试运⾏之前编写的测试。

def city_country(city, country, population=''):
    if population:
        content = f'{city.title()}，{country.title()}-population {population}。'
    else:
        content = f'{city.title()}，{country.title()}。'
    return content