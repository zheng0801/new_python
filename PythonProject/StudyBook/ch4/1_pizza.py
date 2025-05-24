# 想出⾄少三种你喜欢的⽐萨，将其名称存储在⼀个列表中，再使⽤ for 循环将每种⽐萨的名称打印出来。
# 修改这个 for 循环，使其打印包含⽐萨名称的句⼦，⽽不仅仅是⽐萨的名称。对于每种⽐萨都显⽰⼀⾏输出，如下所⽰。
# I like pepperoni pizza.
# 在程序末尾添加⼀⾏代码（不包含在 for 循环中），指出你有多喜欢⽐萨。输出应包含针对每种⽐萨的消息，还有⼀个总结性的句⼦，如下所⽰。
# I really love pizza!

pizzas = ['margherita','napoletana','alla diavola','calzones']

# for pizza in pizzas:
#     print(pizza.title())

for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print(f'我非常喜欢吃披萨，{pizzas[0].title()}是其中味道最好的，{pizzas[1].title()}是我心情不好时最爱的，{pizzas[2].title()}是一个人可以很享受的披萨，{pizzas[3].title}味道更好了')
print('I really love pizza!')
