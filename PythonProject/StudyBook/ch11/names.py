from name_function import get_formatted_name

print('"Enter \'q\' at any time to quit.')

while True:
    first_name = input('\nPlease give me a first name:')
    if first_name == 'q':
        break
    last_name = input('Please give me a last name:')
    if last_name == 'q':
        break

    formatted_name = get_formatted_name(first = first_name, last = last_name)
    print(f'\tNeatly formatted name: {formatted_name}.')