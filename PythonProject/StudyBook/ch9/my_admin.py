# 以为完成练习 9.8 ⽽做的⼯作为基础。将User 类、Privileges 类和 Admin 类存储在⼀个模块中，再创建⼀
# 个⽂件，在其中创建⼀个 Admin 实例并对其调⽤show_privileges() ⽅法，以确认⼀切都能正确地运⾏。

from admin import User, Admin, Privileges

userone = Admin('chen', 'lin', 18, 'male')
userone.privileges.show_privileges()