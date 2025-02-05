
number = float(input("Please enter any number, it would be positive, negative or zero: "))


if number > 0:
    result = "positive"
elif number < 0:
    result = "negative"
else:
    result = "Zero"


print(f"The number {number} is {result} ", )