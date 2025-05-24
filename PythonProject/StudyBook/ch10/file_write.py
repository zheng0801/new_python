
with open('learning_python_write', 'w', encoding = 'utf-8') as f:
    '''w直接覆盖原有内容'''
    f.write('不存在文件，创建一个新文件')
    f.write('在已存在的文件中写入本行')
    lines = ['第一行\n', '第二行\n', '第三行\n']
    f.writelines(lines)#写入多行

with open('learning_python_write', 'a', encoding = 'utf-8') as f:
    '''a的内容会直接补充在末尾'''
    f.write('追加的内容')