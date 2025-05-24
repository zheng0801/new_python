# # 编写一个正则表达式，用于匹配符合中国手机号码格式（11 位数字，以 1 开头）的字符串。
#
# import re
#
# phono_num = input('请输入你的手机号码：')
#
# pattern = r'^1\d{10}'
#
# result = re.findall(pattern, phono_num)
# print(result)

import re

text = "我的手机号码是 13800138000，还有 12345678901 也是手机号。"
pattern = r'1\d{10}'
result = re.findall(pattern, text)
print(result)