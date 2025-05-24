# 创建⼀个字典，在其中存储三条河流及其流经的国家。例如，⼀个键值对可能是 'nile': 'egypt'。
# 使⽤循环为每条河流打印⼀条消息，如下所⽰。
# The Nile runs through Egypt.
# 使⽤循环将该字典中每条河流的名字打印出来。
# 使⽤循环将该字典包含的每个国家的名字打印出来

river = {
    'nile': 'egypt',
    'changjiang': 'china',
    'Amazon': 'brazil',
}

for name, nation in river.items():
    print(f'The {name.title()} runs through {nation.title()}.')

for name in river.keys():
    print(name.title())

for nation in river.values():
    print(nation.title())