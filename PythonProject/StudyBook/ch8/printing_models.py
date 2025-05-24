# 将⽰例 printing_models.py 中的函数放在⼀个名为 printing_functions.py 的⽂件中。在 printing_models.py 的开头编写⼀
# 条 import 语句，并修改这个⽂件以使⽤导⼊的函数。

from printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)