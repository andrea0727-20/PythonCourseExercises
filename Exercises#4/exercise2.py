win_number = 6

while True:
        try:
            guess_number = int(input("Guess a number between 1-10: "))
            if guess_number == win_number:
                 print("Correct you won!!!")
                 break
            elif 1 <= guess_number < win_number:
                 print("Number too low")
            elif guess_number > win_number and guess_number <= 10:
                 print("Number too high")
            else:
                 print("Number out of range, try again!")

        except ValueError:
             print("Invalid input, please enter a number between 1-10.")
