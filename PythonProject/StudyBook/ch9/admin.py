# 管理员是⼀种特殊的⽤户。编写⼀个名为 Admin的类，让它继承你为练习 9.3 或练习 9.5 完成编写的 User 类。添加⼀
# 个名为 privileges 的属性，⽤来存储⼀个由字符串（如 "can add post"、"can delete post"、"can ban user" 等）组成的列
# 表。编写⼀个名为 show_privileges() 的⽅法，显⽰管理员的权限。创建⼀个 Admin 实例，并调⽤这个⽅法。

from user_two import User

# class User:
#     def __init__(self, first_name, last_name, age, gender):
#         self.first_name = first_name
#         self.last_name =last_name
#         self.age = age
#         self.gender = gender
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f'Name: {self.first_name.title()} {self.last_name.title()}')
#         print(f'Age: {self.age}')
#         print(f'Gender: {self.gender}')
#
#     def greet_user(self):
#         print(f'{self.first_name.title()} {self.last_name.title()}，你好啊')
#
#     def increment_login_attempts(self):
#         self.login_attempts +=1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
        # self.privileges = ['can add post', 'can delete post', 'can ban user']

    # def show_privileges(self):
    #     print(self.privileges)

# user = Admin('chen', 'lin', 18, 'female')
# user.show_privileges()

# 编写⼀个名为 Privileges 的类，它只有⼀个属性privileges，其中存储了练习 9.7 所述的字符串列表。将⽅法
# show_privileges() 移到这个类中。在 Admin 类中，将⼀个Privileges 实例⽤作其属性。创建⼀个 Admin 实例，并使⽤⽅法
# show_privileges() 来显⽰权限。

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

# user2 = Admin('chen', 'lin', 30, 'male')
# user2.privileges.show_privileges()