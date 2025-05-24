# 在为练习 6.1 编写的程序中，再创建两个表⽰⼈的字典，然后将这三个字典都存储在⼀个名为 people 的列表中。遍历这
# 个列表，将其中每个⼈的所有信息都打印出来。

people_1 ={
    'first_name': 'zheng',
    'last_name': 'Zheng',
    'age': 20,
    'city': 'fuzhou',
}

people_2 = {
    'first_name': 'lin',
    'last_name': 'Chen',
    'age': 18,
    'city': 'xiamen',
}

people_3 = {
    'first_name': 'zifan',
    'last_name': 'Lin',
    'age': 25,
    'city': 'zhangzhou'
}

people_lists = [people_1, people_2, people_3]

for people in people_lists:
    print(people)

# print(people_lists)