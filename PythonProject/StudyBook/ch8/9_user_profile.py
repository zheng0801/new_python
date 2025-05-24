# 复制前⾯的程序 user_profile.py，在其中调⽤build_profile() 来创建有关你的简介。在调⽤这个函数时，指定
# 你的名和姓，以及三个⽤来描述你的键值对。

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location = 'princeton',
                             field = 'physics')

user_profile_2 = build_profile('zheng', 'zheng',
                               sex = '女',
                               age = 20,
                               educational = '本科')
print(user_profile)
print(user_profile_2)