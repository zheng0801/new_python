# Python 提供了 removesuffix() ⽅法，其⼯作原理与 removeprefix() 很像。请将值 'python_notes.txt'
# 赋给变量 filename，再使⽤ removesuffix() ⽅法来显⽰不包含扩展名的⽂件名，就像⽂件浏览器所做的那样。

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))#去掉后缀
