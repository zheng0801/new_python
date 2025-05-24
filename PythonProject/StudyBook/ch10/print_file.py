# 在⽂本编辑器中新建⼀个⽂件，写⼏句话来总结⼀下你⾄此学到的 Python 知识，其中每⼀⾏都以“In Python
# you can”打头。将这个⽂件命名为 learning_python.txt，并存储到为完成本章练习⽽编写的程序所在的⽬录中。编写⼀个程序，读取这个⽂
# 件，并将你所写的内容打印两次：第⼀次打印时读取整个⽂件；第⼆次打印时先将所有⾏都存储在⼀个列表中，再遍历列表中的各⾏。

with open('learning_python.txt', 'r', encoding = 'utf-8') as f:
    content = f.read()
    content = content.replace('Python', 'Java')
    print(content)

