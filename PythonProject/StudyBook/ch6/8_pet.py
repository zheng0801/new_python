# 创建多个表⽰宠物的字典，每个字典都包含宠物的类型及其主⼈的名字。将这些字典存储在⼀个名为 pets 的列表中，再
# 遍历该列表，并将有关每个宠物的所有信息打印出来。

pet_1 = {
    'type': 'dog',
    'master': 'Zhengzheng',
}

pet_2 = {
    'type': 'cat',
    'master': 'Chenlin',
}

pet_3 = {
    'type': 'bird',
    'master': 'Linyi',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(pet)