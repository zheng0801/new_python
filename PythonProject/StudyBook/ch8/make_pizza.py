import pizza#导入模块pizza，可以使用模块内的所有代码
import pizza as p#导入模块并重命名为p
from pizza import make_pizza#导入模块pizza中的特定函数
from pizza import make_pizza as mp#导入模块中的函数并重命名为mp

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')#导入特定函数的不需要再指明模块

mp(14, 'extra cheese')#重命名行数后的调用

p.make_pizza(14, 'mushrooms')#重命名模块后的调用
