def get_valid_set(prompt):
    while True:
        try:
            user_entry = input(prompt).strip() #stript function deleted extra spaces
            return {int(num) for num in user_entry.split(",")}
        
        except ValueError:
            print("Please, eneter a valid format of the set, Numbers separed by commas: ")

set_entry1 = get_valid_set("Enter the first SET of numbers separed by commas, example: 1,2,3: \n")
set_entry2 = get_valid_set("Enter the second SET of numbers separed by commas, example: 1,2,3: \n")

union_result = set_entry1 | set_entry2
interception_result = set_entry1 & set_entry2
difference_result = set_entry1 - set_entry2

print("The union is: ", union_result )
print("The interception is: ", interception_result)
print("The difference is: ", difference_result)

