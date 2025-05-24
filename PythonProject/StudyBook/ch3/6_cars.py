
cars = ['bmw','audi','toyota','subaru']
cars.sort()#永久的修改列表元素的排序顺序
print(cars)

cars.sort(reverse = True)#字母由降序显示
print(cars)

cars = ['bmw','audi','toyota','subaru']
print(sorted(cars))#对列表元素的顺序进行临时排序
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.reverse()#永久的对列表的元素进行反向打印
print(cars)

print(len(cars))