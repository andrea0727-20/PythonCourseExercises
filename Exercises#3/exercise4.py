while True:
    try:
        number = int(input("Enter a number between 1-7-------> "))
        if 1 <= number <= 7:
            break
        else:
            print("Invalid input. Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

match number:
    case 1:
        result = day_of_week[0]
    case 2:
        result =day_of_week[1]
    case 3:
        result = day_of_week[2]
    case 4:
        result =day_of_week[3]
    case 5:
        result = day_of_week[4]
    case 6:
        result =day_of_week[5]
    case 7:
        result = day_of_week[6]

print(f"The number {number} correspond to: {result}")