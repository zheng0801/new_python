# 将最新的 Restaurant 类存储在⼀个模块中。在另⼀个⽂件中导⼊ Restaurant 类，创建⼀个
# Restaurant 实例，并调⽤ Restaurant 的⼀个⽅法，以确认import 语句正确⽆误。

from restaurant import Restaurant

favorite_restaurant = Restaurant('好再来', '川味')
favorite_restaurant.describe_restaurant()