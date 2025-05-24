
rivers = ['minjiang','changjiang','huanghe','zhujiang']
print(rivers)

print(rivers[2])

print(f'离我最近的河是：{rivers[0].title()}')

rivers[3] = 'qiantangjiang'
print(rivers)

rivers.append('taoxi')
print(rivers)
rivers.insert(2,'jinjiang')
print(rivers)

del rivers[4]
print(rivers)

popped_river = rivers.pop()
print(rivers)
print(popped_river)
popped_river = rivers.pop(1)
print(rivers)
print(popped_river)
rivers.remove('huanghe')
print(rivers)

rivers = ['minjiang','changjiang','huanghe','zhujiang']
print(rivers)
rivers.sort()
print(rivers)
rivers.sort(reverse = True)
print(rivers)

rivers = ['minjiang','changjiang','huanghe','zhujiang']
print(sorted(rivers))
print(rivers)
print(sorted(rivers,reverse = True))
print(rivers)

rivers = ['minjiang','changjiang','huanghe','zhujiang']
rivers.reverse()
print(rivers)
rivers.reverse()
print(rivers)

print(len(rivers))
print(rivers[-5])
