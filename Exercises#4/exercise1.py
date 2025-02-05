number = float(input("Enter a number: "))

print(f"Multiplication table of {number}:")

for i in range(1,11):
    result = number * i
    print(f"The number {number} X {i} = {result}")