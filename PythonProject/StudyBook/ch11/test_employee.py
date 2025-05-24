# 为 Employee 类编写⼀个测试⽂件，其中包含两个测试函数：test_give_default_raise() 和
# test_give_custom_raise()。在不使⽤夹具的情况下编写这两个测试，并确保它们都通过了。然后，编写⼀个夹具，以免在每个测试
# 函数中都创建⼀个 Employee 对象。重新运⾏测试，确认两个测试都通过了。
import pytest
from employee import Employee

@pytest.fixture
def salary_employee():
    salary_employee = Employee('lin', 'wang', 6000)
    return salary_employee

# def test_give_default_raise():
#     '''测试默认值薪水添加'''
#     employee_one = Employee('zheng', 'chen', 5000)
#     employee_one.give_raise()
#     assert employee_one.annual_salary == 10000
#
# def test_give_custom_raise():
#     '''测试任意薪水添加'''
#     employee_two = Employee('chen', 'lin', 5000)
#     employee_two.give_raise(2000)
#     assert employee_two.annual_salary == 7000

def test_give_default_raise(salary_employee):
    salary_employee.give_raise()
    assert salary_employee.annual_salary == 11000

def test_give_custom_raise(salary_employee):
    salary_employee.give_raise(4000)
    assert salary_employee.annual_salary == 10000