# Exercises ➞ Level 3:
# import keyword

# 1. Write a function called is_prime, which checks if a number is prime.

def is_prime():
    num = int(input("Enter a positive integer: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                return True
    return False

if is_prime():
    print("This is a Prime Number")
else:
    print("This is not a Prime Number")

# 2. Write a functions which checks if all items are unique in the list.

def unique_items_list():
    input_list = input("Enter a list: ").split()
    st = set(input_list)
    if len(input_list) == len(st):
        return True
    else:
        return False

if unique_items_list():
    print("All items are unique in the list")
else:
    print("All items are not unique in the list")

# 3. Write a function which checks if all the items of the list are of the same data type.

def same_datatype_list(lst):
    for item in lst:
        if type(item) == type(lst[0]):
            continue
        else:
            return False
    return True

in_list = [1, 2, "a", (1, 2)]

if same_datatype_list(in_list):
    print(f"All items in the list: {in_list} are of same datatype")
else:
    print(f"All items in the list: {in_list} are not of same datatype")

# 4. Write a function which checks if provided variable is a valid python variable

def valid_variable():
    var = input("Enter a variable name: ")
    # need to import keyword to make additional checks. (var not in keyword.kwlist)
    return var[0].isalpha() or var[0] == "_"

if valid_variable():
    print("Valid variable")
else:
    print("Invalid variable")

# 5. Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries.
# It should return 10 or 20 most populated countries in descending order.

'''Not able to access countries-data.py file'''

def most_spoken_languages():
    pass

def most_populated_countries():
    pass



