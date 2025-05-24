# 创建⼀个 Die 类，它包含⼀个名为 sides 的属性，该属性的默认值为 6。编写⼀个名为 roll_die() 的⽅法，它打印位
# 于 1 和骰⼦⾯数之间的随机数。创建⼀个 6 ⾯的骰⼦并掷 10 次。
# 创建⼀个 10 ⾯的骰⼦和⼀个 20 ⾯的骰⼦，再分别掷 10 次。

from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        num = 1
        while num <= 10:
            print(randint(1, self.sides))
            num += 1

# die = Die()
# die.roll_die()

die_two = Die(10)
die_two.roll_die()

