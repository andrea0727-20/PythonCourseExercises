character = input("Enter a single character (vowel, consonant, digit, or special character) ---> ")

vowels = {'a', 'e', 'i', 'o', 'u'}

if len(character) != 1:
    result = "Invalid input. Please enter a single character."

elif character.lower() in vowels:
    result = "Vowel"
elif character.isalpha():
    result = "Consonant"
elif character.isdigit():
    result = "Digit"
else:
    result = "Special character"


print(f"The charater is: {result}")