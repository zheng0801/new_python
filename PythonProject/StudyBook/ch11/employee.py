# 编写⼀个名为 Employee 的类，其 __init__() ⽅法接受名、姓和年薪，并将它们都存储在属性中。编写⼀个名为
# give_raise() 的⽅法，它默认将年薪增加 5000 美元，同时能够接受其他的年薪增加量。


class Employee:

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, salary=5000):
        self.annual_salary += salary