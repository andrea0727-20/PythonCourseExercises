def get_boolean_input(prompt):
    values = {"true": True, "false": False}
   
    while True:
        (value := input(prompt).strip().lower())
        if value in values:
            return values[value]
        else:
            print("Invalid value. Please entter just True or False: ")

value_1= get_boolean_input("Enter the first boolean value True/False: ")
value_2= get_boolean_input("Enter the second boolean value True/False: ")

# Logic operations assessment 
print("Results \n")
print(f"{value_1} AND {value_2} -> {value_1 and value_2}")
print(f"{value_1} OR {value_2} -> {value_1 or value_2}")
print(f"NOT {value_1} -> {not value_1}")
print(f"NOT {value_2} -> {not value_2}")
      





