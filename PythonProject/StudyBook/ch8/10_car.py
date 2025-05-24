# 编写⼀个函数，将⼀辆汽⻋的信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。在
# 调⽤这个函数时，提供必不可少的信息，以及两个名值对，如颜⾊和选装配件。这个函数必须能够像下⾯这样调⽤：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。

def make_car(name, type, **car_info):
    car_info['manufacturer'] = name
    car_info['car_type'] = type
    return car_info

car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)

print(car)
