win_number = 6
attempts = 3

question = ('Could you please guess a number between 1 and 10? : \n'
        '---- Remember that you have just 3 attemps -----')
print(question )
for i in range(attempts):
    try:
    
        user_answer  = int(input(f'Attemp number {i+1}/{attempts}: '))

        if user_answer < 1 or user_answer > 10:
            print("Invalid number! Please enter a number between 1 and 10.")
            continue 

        if user_answer == win_number:
            print('You are the winner!!!!')
            break
        else:
            print('Try again X')

    except ValueError:
        print("Invalid digit, just between 1-10")
        
else:
    print(f'Game Over :::::/) The number was ---> {win_number}')

