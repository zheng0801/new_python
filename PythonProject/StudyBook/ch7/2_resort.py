# 编写⼀个程序，调查⽤户梦想中的度假胜地。使⽤类似于“If you could visit one place in the world, where
# would you go?”的提⽰，并编写⼀个打印调查结果的代码块。

resorts = {}
action = True

while action:
    name = input('What\'s your name: ')
    place = input('If you could visit one place in the world, where would you go? ')

    resorts[name] = place

    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        action = False

for name, place in resorts.items():
    print(f'{name.title()} want to go {place.title()}')