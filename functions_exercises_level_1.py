# Exercises ➞ Level 1:

# 1. Area of a circle is calculated as follows: area = π x r x r and perimeter = 2 x π x r.
# Write a function that calculates area_of_circle and perimeter_of_circle.

def circle_area_and_perimeter():
    r = float(input("Enter the radius: "))
    perimeter = 2 * 3.14 * r
    area = 3.14 * r * r
    return r, perimeter, area

rad, peri, ar = circle_area_and_perimeter()
print(f"Radius of Circle: {rad}, Perimeter: {peri}, Area: {ar}")

# 2. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums():
    num_list = list((input("Enter numbers (separated with space): ")).split())
    sum_all_nums = 0
    for num in num_list:
        if num.isdigit():
            sum_all_nums += int(num)
        else:
            print("Invalid input! Please input only integer values separated by a space (e.g.: 1 2 3 4).")
            exit()

    return sum_all_nums

print(f"Sum of all numbers: {add_all_nums()}")

# 3. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_2_fahrenheit.

def convert_celsius_2_fahrenheit():
    temp_c = float(input("Enter the temperature in Celsius: "))
    temp_f = (temp_c * 9/5) + 32
    return temp_f

print(f"Temperature in Fahrenheit: {convert_celsius_2_fahrenheit()}")

# 4. Write a function called check_season,
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    season_dict = {"Spring": ["february", "march", "april"], "Summer": ["may", "june", "july"],
                   "Autumn": ["august", "september", "october"], "Winter": ["november", "december", "january"]}
    for key, values in season_dict.items():
        if month in values:
            return key
    return f"{month} is not a valid month name"

m = input("Enter the name of a month: ")
print(check_season(m))

# 5. Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope():
    x, y = tuple(input("Enter x, y: ").split())
    x1, y1 = tuple(input("Enter x1, y1: ").split())
    m = (int(y1) - int(y))/(int(x1) - int(x))
    return m
print(calculate_slope())

# 6. Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn():
    eq = "ax² + bx + c = 0"
    # discriminant = (b*b) - (4*a*c)
    pass

# 7. Declare a function named print_list.
# It takes a list as a parameter, and it prints out each element of the list.

def print_list(input_list: list):
    for element in input_list:
        print(element)

il = [1, (2, 6), "t", 9.5]
print_list(il)

# 8. Declare a function named reverse_list.
# It takes an array as a parameter, and it returns the reverse of the array (use loops).

def reverse_list(input_list: list):
    reverse = []
    for item in input_list[::-1]:
        reverse.append(item)
    return reverse

print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 9. Declare a function named capitalize_list_items.
# It takes a list as a parameter, and it returns a capitalized list of items.

def capitalize_list_items(input_list: list):
    capitalized_list = []
    for item in input_list:
        capitalized_list.append(item.capitalize())
    return capitalized_list

print(capitalize_list_items(["name", "adDress", "1234"]))

# 10. Declare a function named add_item.
# It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(input_list: list, item):
    input_list.append(item)
    return input_list

print(add_item([1, 2, "a"], 4.5))


# 11. Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.

# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango')) Output: ['Potato', 'Tomato', 'Milk']
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3)) Output: [2, 7, 9]

def remove_item(input_list: list, item):
    input_list.remove(item)
    return input_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

# 12. Declare a function named sum_of_numbers.
# It takes a number parameter, and it adds all the numbers in that range.

def sum_of_numbers(number):
    result = 0
    for num in range(number+1):
        result += num
    return result

print(sum_of_numbers(10))

# 13. Declare a function named sum_of_odds.
# It takes a number parameter, and it adds all the odd numbers in that range.

def sum_of_odds(number):
    result = 0
    for num in range(number+1):
        if num % 2 != 0:
            result += num
    return result

print(sum_of_odds(10))

# 14. Declare a function named sum_of_even.
# It takes a number parameter, and it adds all the even numbers in that - range.

def sum_of_even(number):
    result = 0
    for num in range(number+1):
        if num % 2 == 0:
            result += num
    return result

print(sum_of_even(10))


