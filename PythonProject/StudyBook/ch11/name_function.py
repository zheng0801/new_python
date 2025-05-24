
def get_formatted_name(first, last, middle=''):
    #拼接姓名，并返回拼接后首字母大写的姓名
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()