# 选择你在本章编写的⼀个程序，在末尾添加⼏⾏代码，以完成如下任务。
# 打印消息“The first three items in the list are:”，再使⽤切⽚来打印列表的前三个元素。
# 打印消息“Three items from the middle of the list are:”，再使⽤切⽚来打印列表中间的三个元素。
# 打印消息“The last three items in the list are:”，再使⽤切⽚来打印列表末尾的三个元素。

numbers = list(number ** 3 for number in range(1,11))#对应的立方推导式

# for number in numbers:
#     print(number)

for number in numbers[:3]:
    print(f"The first three items in the list are:{number}")

for number in numbers[3:6]:
    print(f'There items from the middle of the list are:{number}')
    
for number in numbers[-3:]:
    print(f'The last three items in the list are:{number}')


