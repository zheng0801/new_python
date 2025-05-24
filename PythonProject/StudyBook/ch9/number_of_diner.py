# 在为练习 9.1 编写的程序中，添加⼀个名为number_served 的属性，并将其默认值设置为 0。根据这个类创建⼀
# 个名为 restaurant 的实例。打印有多少⼈在这家餐馆就餐过，然后修改这个值并再次打印。
# 添加⼀个名为 set_number_served() 的⽅法，⽤来设置就餐⼈数。调⽤这个⽅法并向它传递新的就餐⼈数，然后再次打印这个值。
# 添加⼀个名为 increment_number_served() 的⽅法，⽤来让就餐⼈数递增。调⽤这个⽅法并向它传递⼀个这样的值：你认为这家餐馆
# 每天可能接待的就餐⼈数。

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

restaurant = Restaurant('好再来', '川菜馆')
restaurant.describe_restaurant()
restaurant.set_number_served(8)
