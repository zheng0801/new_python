# 利用条件运算符的嵌套来完成此题:学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = float(input('请输入您要查询等级的成绩：'))

if score >= 90:
    level = 'A'
elif score >= 60:
    level = 'B'
else:
    level = 'C'

print(f'{int(score)}对应的等级是：{level}')