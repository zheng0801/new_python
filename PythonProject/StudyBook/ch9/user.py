# 创建⼀个名为 User 的类，其中包含属性first_name 和 last_name，还有⽤户简介中通常会有的其他⼏个属性。
# 在类 User 中定义⼀个名为 describe_user() 的⽅法，⽤于打印⽤户信息摘要。再定义⼀个名为 greet_user() 的⽅法，⽤于向
# ⽤户发出个性化的问候。创建多个表⽰不同⽤户的实例，并对每个实例调⽤上述两个⽅法。

class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name =last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f'Name: {self.first_name.title()} {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

    def greet_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}，你好啊')

zheng = User('zheng', 'zheng', 20, 'female')
chen = User('chen', 'lin', 18, 'male')

zheng.describe_user()
zheng.greet_user()
chen.describe_user()
chen.greet_user()