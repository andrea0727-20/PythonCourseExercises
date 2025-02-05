string = input("Enter a string: ")

vowels = {'a', 'e', 'i', 'o', 'u'}
count_vowels = 0

for char in string:
    if char.lower() in vowels:
        count_vowels += 1
print(f"The number of vowels in the string is: {count_vowels}")
