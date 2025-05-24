
import json

with open('number.json', 'r', encoding = 'utf-8') as file:
    contents = file.read()
    numbers = json.loads(contents)
    print(numbers)