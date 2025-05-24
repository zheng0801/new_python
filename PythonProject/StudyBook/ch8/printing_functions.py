# 将⽰例 printing_models.py 中的函数放在⼀个名为 printing_functions.py 的⽂件中。在 printing_models.py 的开头编写⼀
# 条 import 语句，并修改这个⽂件以使⽤导⼊的函数。

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nThe following models have been printed.')
    for completed_model in completed_models:
        print(completed_model)
