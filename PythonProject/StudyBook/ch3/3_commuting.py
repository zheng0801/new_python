# 想想你喜欢的通勤⽅式，如骑摩托⻋或开汽⻋，并创建⼀个包含多种通勤⽅式的列表。
# 根据该列表打印⼀系列有关这些通勤⽅式的陈述，如下所⽰。
# I would like to own a Honda motorcycle.

commuting = ['bicycle','car','motorcycle','bus']

for i in range(len(commuting)):
    print(f'I would like to own a {commuting[i].title()}.')
