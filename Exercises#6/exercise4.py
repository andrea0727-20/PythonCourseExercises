def find_max_number():
    while True:
        try:
            numbers = input("Enter a list of numbers separed by commas: ").strip()
            if len(numbers) == 0:
                print("The list not should be empty. Try again")
                continue
            
            numbers = [float(num.strip()) for num in numbers.split(",")]

            if numbers:
                break
        except ValueError:
            print("Invalid format. Please enter numbers separated by commas.")
   
    max_number = max(numbers)

    print(f"The largest number in the list is {max_number}")
    return max_number

find_max_number()