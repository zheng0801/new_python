# 访问古登堡计划，找⼀些你想分析的图书。下载这些作品的⽂本⽂件或将浏览器中的原始⽂本复制到⽂本⽂件中。
# 可以使⽤⽅法 count() 来确定特定的单词或短语在字符串中出现了多少次。例如，下⾯的代码计算 'row' 在⼀个字符串中出现了多少次：
# 请注意，通过使⽤ lower() 将字符串转换为全⼩写的，可捕捉要查找的单词的各种格式，⽽不管其⼤⼩写如何。
# 编写⼀个程序，读取你在古登堡计划中获取的⽂件，并计算单词'the' 在每个⽂件中分别出现了多少次。这⾥计算得到的结果并不准
# 确，因为诸如 'then' 和 'there' 等单词也被计算在内了。请尝试计算 'the '（包含空格）出现的次数，看看结果相差多少。

single = input('请输入你要查询的单词：')

try:
    with open('book.txt', 'r', encoding = 'utf-8') as file:
        content = file.read().lower()
except FileNotFoundError:
    print('文件不存在！')
else:
    total = content.count(single.lower())
    print(total)
