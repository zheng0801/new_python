# 编写⼀个名为 favorite_book() 的函数，其中包含⼀个名为 title 的形参。让这个函数打印⼀条像下⾯这样的消息。
# One of my favorite books is Alice in Wonderland.调⽤这个函数，并将⼀本书的书名作为实参传递给它。

def favorite_book(title):
    print(f'One of my favorite books is Alice in {title.title()}')

favorite_book('one day')
