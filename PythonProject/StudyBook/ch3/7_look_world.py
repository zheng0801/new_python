# 放眼世界 想出⾄少 5 个你想去旅游的地⽅。
# 将这些地⽅存储在⼀个列表中，并确保其中的元素不是按字⺟顺序排列的。
# 按原始排列顺序打印该列表。不要考虑输出是否整洁，只管打印原始 Python 列表就好。
# 使⽤ sorted() 按字⺟顺序打印这个列表，不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使⽤ sorted() 按与字⺟顺序相反的顺序打印这个列表，不要修改它。
# 再次打印该列表，核实排列顺序未变。
# 使⽤ reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
# 使⽤ reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
# 使⽤ sort() 修改该列表，使其元素按字⺟顺序排列。打印该列表，核实排列顺序确实变了。
# 使⽤ sort() 修改该列表，使其元素按与字⺟顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。

places = ['changsha','beijing','shanghai','fuzhou','anhui']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)



