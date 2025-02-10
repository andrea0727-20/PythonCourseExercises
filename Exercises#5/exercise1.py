user_entry = input("Enter a list of numbers separated by spaces: ")

user_list_to_integer = list(map(int, user_entry.split())) # another option ---> user_list_to_integer = [int(num) for num in user_entry.split()]
print("The list is: ",user_list_to_integer)
print("The lenght is: ", len(user_list_to_integer))
print("The smallest number is: ", min( user_list_to_integer))
print("The largest number is: ", max( user_list_to_integer))
