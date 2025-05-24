# 编写⼀个名为 make_shirt() 的函数，它接受⼀个尺码以及要印到 T 恤上的字样。这个函数应该打印⼀个句⼦，
# 简要地说明 T 恤的尺码和字样。先使⽤位置实参调⽤这个函数来制作⼀件 T 恤，再使⽤关键字实参来
# 调⽤这个函数。

# def make_shirt(size,typeface):
#     print(f'要在{size}尺寸的T-恤上打印{typeface}')
#
# make_shirt(28, '雅黑')#位置实参
# make_shirt('雅黑', 28)
# make_shirt(typeface = '雅黑', size = 30)#关键字实参

# 修改 make_shirt() 函数，使其在默认情况下制作⼀件印有
# “I love Python”字样的⼤号 T 恤。调⽤这个函数分别制作⼀件印有默认
# 字样的⼤号 T 恤，⼀件印有默认字样的中号 T 恤，以及⼀件印有其他字样的 T 恤（尺码⽆关紧要）。

def make_shirt(size = 'large', typeface = 'I love Python'):
    print(f'要在{size.title()}尺寸的T-恤上打印{typeface}')

make_shirt()
make_shirt(size = 'medium')
make_shirt(typeface = '这是其他字样的T恤')