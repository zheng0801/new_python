
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'#修改指定索引位置的元素
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki']

motorcycles.append('ducati')#在列表末尾添加一个元素
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki']

motorcycles.insert(1,'ducati')#在指定索引处添加元素
print(motorcycles)

del motorcycles[1]#删除指定索引位置的元素
print(motorcycles)


motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()#弹出列表末尾的元素并赋值
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop(1)#弹出指定索引位置的元素并赋值
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('suzuki')#删除列表中指定的值，只删除第一个指定的值，列表中有多个相同的值，需要用循环来删除
print(motorcycles)