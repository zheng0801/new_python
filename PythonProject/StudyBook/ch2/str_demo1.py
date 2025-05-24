first_name = 'ada'
last_name = 'sky'
full_name = f'{first_name} {last_name}'#字符串拼接
print(full_name)

print(full_name.title())#首字母大写
print(full_name.upper())#全部大写
print(full_name.lower())#全部小写

favorite_language = ' python '

print(favorite_language.strip())#去掉两边的空白
print(favorite_language.lstrip())#去掉左侧的空白
print(favorite_language.rstrip())#去掉右侧的空白

test_url = 'https://192.168.10.8:11000/login?redirect=%2Findex'
print(test_url.removeprefix('https://'))#删除前缀
#print(test_url.removeprefix('/login?redirect=%2Findex'))#无效，无法删除其他位置的内容
simple_url = test_url.removeprefix('https://')
print(simple_url)