
print("This program needs type 2 numbers and an operator(+, -, *, /). \n")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter the operator between (+, -, *, /): ")


match operator:
    case '+':
        result = number1 + number2
    case '-':
        result = number1 - number2
    case '*':
        result = number1 * number2
    case '/':
        result = number1 / number2 if number2 != 0 else 'Undefined: Cannot divide by zero'
    case _:
        result = 'Invalid operator'

print(f'The operation result is -> {number1} {operator} {number2} = {result}')

