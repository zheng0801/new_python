# 在为练习 9.3 编写的 User 类中，添加⼀个名为 login_attempts 的属性。编写⼀个名为
# increment_login_attempts() 的⽅法，⽤来将属性login_attempts 的值加 1。再编写⼀个名为
# reset_login_attempts() 的⽅法，⽤来将属性login_attempts 的值重置为 0。根据 User 类创建⼀个实例，再调⽤
# increment_login_attempts() ⽅法多次。打印属性login_attempts 的值，确认它正确地递增了。然后，调⽤⽅法
# reset_login_attempts()，并再次打印属性 login_attempts的值，确认它被重置为 0。

class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name =last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f'Name: {self.first_name.title()} {self.last_name.title()}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')

    def greet_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}，你好啊')

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts = 0

# user1 = User('zheng', 'zheng', 18, 'female')
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.increment_login_attempts()
# print(user1.login_attempts)
# user1.reset_login_attempts()
# print(user1.login_attempts)
