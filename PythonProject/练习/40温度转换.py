# 输入摄氏度，将其转为华氏度。
# 输入华氏度，将其转为摄氏度。
# 华氏温度与摄氏温度转换公式为:华氏温度=摄氏温度x1.8+32。

def convert(n, m):
    if n == '1':
        return (m -32) / 1.8
    elif n =='2':
        return m * 1.8 + 32

a = input('输入华氏度请按1，摄氏度请按2：')

if a == '1':
    f = float(input('请输入华氏度：'))
    print(f'你输入的是华氏度{f}，转换成摄氏度后是：{convert(a, f):.2f}')
elif a == '2':
    d = float(input('请输入摄氏度：'))
    print(f'你输入的是摄氏度{d}，转换成华氏度后是：{convert(a, d):.2f}')
