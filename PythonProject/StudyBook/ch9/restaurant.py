# 创建⼀个名为 Restaurant 的类，为其__init__() ⽅法设置两个属性：restaurant_name 和
# cuisine_type。创建⼀个名为 describe_restaurant() 的⽅法和⼀个名为 open_restaurant() 的⽅法，其中前者打印前述两项信
# 息，⽽后者打印⼀条消息，指出餐馆正在营业。根据这个类创建⼀个名为 restaurant 的实例，分别打印其两个属性，再调⽤前述两个⽅法。

class Restaurant:
    def __init__(self, restaurant_name, cuisine_name):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name

    def describe_restaurant(self):
        print(f'{self.restaurant_name} {self.cuisine_name}')

    def open_restaurant(self):
        print('餐馆正在营业中')

# favorite_restaurant = Restaurant('好味道', '川菜馆')
#
# print(favorite_restaurant.restaurant_name)
# print(favorite_restaurant.cuisine_name)
# favorite_restaurant.describe_restaurant()
# favorite_restaurant.open_restaurant()
#
# # 根据为练习 9.1 编写的类创建三个实例，并对每个实例调⽤ describe_restaurant() ⽅法。
#
# your_restaurant = Restaurant('好再来', '烤鱼')
# your_restaurant.describe_restaurant()