def is_leap_year(year: int):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

while True:
    try:
        year = int(input('Enter a year: '))
        if is_leap_year(year):
            print(f'The {year} is a leap year! ')
        else:
            print(f'The {year} is not a leap year! ')
        break
    except ValueError:
        print("Invalid year. Please enter a valid year.")