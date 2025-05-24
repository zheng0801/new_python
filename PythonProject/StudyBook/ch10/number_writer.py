import json

numbers = ['2', '4', '6', '8', '10']

with open('number.json', 'w', encoding = 'utf-8') as file:
    content = json.dumps(numbers)
    file.write(content)