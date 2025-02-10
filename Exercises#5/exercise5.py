
user_entry = input("Enter a sentence: ")

words= user_entry.lower()

count_chars = {}

for char in words:
    if char in count_chars:
        count_chars[char] +=1
    else:
        count_chars[char] = 1

print("Character frequency count:")
for char , count in count_chars.items():
    print(f"{char}: {count}")
