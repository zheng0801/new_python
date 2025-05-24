# 在本节中，为节省篇幅，程序 foods.py 的每个版本都没有使⽤ for 循环来打印列表。请选择⼀个版本的
# foods.py，在其中编写两个 for 循环，将各个⾷品列表都打印出来。

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)

for food in my_foods:
    print(f'My favorite foods are: {food}')

for food in friend_foods:
    print(f'My friend\'s favorite foods are: {food}')