try:
    message = 'How old are you:? '
    age = int(input(message))
   # print('You have' + ' ', str(age) + 'years') one option
    print(f'You have {age} years')
except ValueError:
    print("It's not a valid age")
