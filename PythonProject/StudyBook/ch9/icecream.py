# 让它继承你为练习 9.1 或练习 9.4 编写的Restaurant 类。这两个版本的 Restaurant 类都可以，挑选你更喜
# 欢的那个即可。添加⼀个名为 flavors 的属性，⽤于存储⼀个由各种口味的冰激凌组成的列表。编写⼀个显⽰这些冰激凌口味的⽅法。创
# 建⼀个 IceCreamStand 实例，并调⽤这个⽅法。

class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.number_serves = 0

    def describe_restaurant(self):#打印餐厅信息
        print(f'{self.restaurant_name} {self.cuisine_name}')

    def open_restaurant(self):#餐厅状态
        print('餐馆正在营业中')

    def set_number_served(self, number):#设置就餐人数
        self.number_serves = number
        print(self.number_serves)

    def increment_number_served(self, number):#就吃人数递增
        self.number_serves += number


class IceCreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_name):
        super().__init__(restaurant_name, cuisine_name)
        self.flavors = []

    def print_flavors(self):#打印冰淇淋口味
        for flavor in self.flavors:
            print(flavor)

    def set_flavors(self,flavor):#添加冰淇淋口味
        self.flavors.append(flavor)

icecreamstand = IceCreamstand('冰淇淋店', '甜品')

icecreamstand.describe_restaurant()

icecreamstand.set_flavors('抹茶')
icecreamstand.set_flavors('巧克力')
icecreamstand.set_flavors('白桃')
icecreamstand.print_flavors()
