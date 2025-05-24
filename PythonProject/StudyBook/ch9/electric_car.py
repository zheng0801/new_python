# 在本节最后⼀个 electric_car.py 版本中，给Battery 类添加⼀个名为 upgrade_battery() 的⽅法。这个⽅法
# 检查电池容量，如果电池容量不是 65，就设置为 65。创建⼀辆电池容量为默认值的电动汽⻋，调⽤⽅法 get_range()，然后对电池进⾏升
# 级，并再次调⽤ get_range()。你将看到这辆汽⻋的续航⾥程增加了。


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):#打印车辆信息年份、类型等
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):#打印车辆里程数
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):#更新车辆里程数
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):#增加车辆里程数
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=40):#初始化电池属性
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

    def describe_battery(self):#打印电池容量信息
        print(f'This car has a {self.battery_size}-KWh battery.')

    def get_range(self):#打印电池续航里程
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f'This car can go about {range} miles on a full charge.')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


carone = ElectricCar('nissan', 'leaf', 2024)
carone.battery.get_range()
carone.battery.upgrade_battery()
carone.battery.get_range()


