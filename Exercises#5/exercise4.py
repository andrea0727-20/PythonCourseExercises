def get_valid_dict(prompt):
    while True:
        try:
            user_entry = input(prompt).strip() #stript function deleted extra spaces
            return (user_entry.split(","))
        except ValueError:
            print("Please enter the correct format, example: string1, string2, string3...")

while True:
    user_keys = get_valid_dict("Enter please a list of keys separated by commas: ")
    user_values = get_valid_dict("Enter please a list of values separated by commas: ")

    if len(user_keys) != len(user_values):
        print("Error: The among of keys and values is not the same, please try again")
    else:
        dict_created = dict(zip(user_keys, user_values))
        print("The diccionary created is: ", dict_created)
        break