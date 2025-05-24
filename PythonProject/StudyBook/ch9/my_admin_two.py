# 将 User 类存储在⼀个模块中，并将Privileges 类和 Admin 类存储在另⼀个模块中。再创建⼀个⽂件，
# 在其中创建⼀个 Admin 实例并对其调⽤ show_privileges() ⽅法，以确认⼀切依然能够正确地运⾏。

from user_two import User
from admin import Admin, Privileges

usertwo = Admin('lin', 'wang', 20, 'male')
usertwo.privileges.show_privileges()