# __SET 1__:

# 1. Enter number until 0. print sum of all even numbers
# num_list = []
# result = 0
# while True:
#     user_input = input("Enter a number (0 to stop): ")
#     if user_input == "0":
#         break
#     elif user_input.isdigit():
#         num_list.append(int(user_input))
#     else:
#         continue
#
# for num in num_list:
#     if num % 2 == 0:
#         result += num
#
# print(result)

# 2. Student Grade Classifier:
# Input 3 subject marks. Use if-elif-else to assign grade:
# ≥90 → A
# 75-89 → B
# 60-74 → C
# <60 → F

# marks = {}
# subjects = ["Math", "Science", "English"]
# for subject in subjects:
#     marks.update({subject: int(input(f"Enter marks for {subject}: "))})
#
# average = sum(marks.values()) / len(marks)
# print(f"Average marks: {average}")
#
# if 100 >= average >= 90:
#     print("Grade: A")
# elif 75 <= average <= 89:
#     print("Grade: B")
# elif 60 <= average <= 74:
#     print("Grade: C")
# elif average < 60:
#     print("Grade: F")
# else:
#     print("Invalid Marks! Please enter marks between 0 and 100.")

# 3. Tuple Processor:
# Given a list of tuples like [(10, 2), (5, 0), (8, 4)], divide first by second only if second is not zero.

#Approach 1
# list_of_tuples = [(10, 2), (5, 0), (8, 4)]
# for a, b in list_of_tuples:
#     if b != 0:
#         print(a/b)

# Approach 2
# a=[(10, 2), (5, 0), (8, 4)]
# for i in range(len(a)):
#     if a[i][1]==0:
#         continue
#     print(a[i][0]/a[i][1])

# 4. Flatten Dictionary:
# Given a dictionary like:
#  	data = {"a": 1, "b": {"x": 2, "y": 3}}
#  	Output: {"a": 1, "b.x": 2, "b.y": 3}

# data = {"a": 1, "b": {"x": 2, "y": 3}}
# flattened_data = {}
# for key, value in data.items():
#     if isinstance(value, dict):
#         for sub_key, sub_value in value.items():
#             flattened_data.update({f"{key}.{sub_key}": sub_value})
#     else:
#         flattened_data.update({key: value})
# print(flattened_data)

# 5. Hollow Pyramid Pattern with Numbers:
# Input = 5
# Output:
#  	  1
#    1 2
#   1   3
#  1     4
# 1 2 3 4 5

# rows = input("Enter the number of rows: ")
# rows_list = []
#
# if rows.isdigit():
#     rows = int(rows)
# else:
#     print("Please enter a valid number.")
#     exit()
#
# for i in range(1, rows+1):
#     print(" "*(rows-i), end="")
#     rows_list.append(i)
#     if i == 1:
#         print(i)
#     elif i == rows:
#         print(*rows_list)
#     else:
#         print(rows_list[0], " "*(2*(i-2)+1), rows_list[-1], sep="")


# __SET 2__:

# 1. Calculate BMI:
# Take height and weight from user, compute BMI = weight/height^2, and print result.
# height = input("Enter your height in meters: ")
# weight = input("Enter your weight in kilograms: ")
#
# try:
#     height = float(height)
#     weight = float(weight)
#     bmi = weight/(height**2)
#     print(f"Your BMI is: {bmi}")
# except ValueError:
#     print("Please enter valid numbers for height and weight.")
#     exit()

# 2. Odd-Even counter in list:
# Given a list, count how many numbers are odd vs even.
# numbers = [1, 2, 3]
# even_count = 0
# odd_count = 0
# for number in numbers:
#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count+=1
# print(f"There are {even_count} even numbers and {odd_count} odd numbers in the list.")

# 3. Login Validation:
# Input username and password.
# If username is correct:
#   Check password
#   Else invalid password
# Else invalid user

# username = input("Enter Username: ")
# password = input("Enter Password: ")
# correct = {"username": "admin", "password": "admin@123"}
# if username == correct["username"]:
#     if password == correct["password"]:
#         print("Login Successful!")
#     else:
#         print("Invalid Password")
# else:
#     print("Invalid Username")

# 4. Flatten Dictionary with mixed types:
# Input: {"x": 10, "y": {"a": 5, "b": {"z": 1}}}
# Output: {'x': 10, 'y.a': 5, 'y.b.z': 1}

# input_dict = {"x": 10, "y": {"a": 5, "b": {"z": 1}}}
# flattened_dict = {}
# recursion_tracker = [(input_dict, "")]
#
# while recursion_tracker:
#     current_dict, key_prefix = recursion_tracker.pop()
#     for key, value in current_dict.items():
#         if key_prefix:
#             new_key = f"{key_prefix}.{key}"
#         else:
#             new_key = key
#         if isinstance(value, dict):
#             recursion_tracker.append((value, new_key))
#         else:
#             flattened_dict[new_key] = value
#
# print(flattened_dict)

# 5. Hourglass Star Pattern:
# Input: 5
# Output:
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********

# n1 = 5
# for i in range(1, n1 + 1):
#     print(" "*i+"*"*((n1*2)-1))
#     n1-=1
# n2 = 5
# for j in range(2, n2 + 1):
#     print(" "*(n2-1)+"*"*((j*2)-1))
#     n2-=1


# __SET 3__:

# 1. Add two Floats and Print Boolean:
# Input two float values. Print True if their sum > 100, else False.
# float1 = input("Enter first float value: ")
# float2 = input("Enter second float value: ")
# print(float(float1) + float(float2) > 100)

# 2. Reverse List manually:
# Input a list of integers and reverse it manually (no slicing).
# input_list = [1, 2, 3]
# reversed_list = []
# for i in input_list:
#     reversed_list.insert(0,i)
# print(reversed_list)

# 3. Leap year checker:
# A year is leap if:
#    - Div by 4 and not by 100 or
#    - Div by 400
# year = input("Enter a year: ")
# if year.isdigit():
#     year = int(year)
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# else:
#     print("Please enter a valid year in numeric format.")

# 4. Flatten List of Dicts to Single Dict:
# Given: [{'a': 1}, {'b': 2, 'c': 3}, {'d': {'e': 4}}]
# Output: {'a': 1, 'b': 2, 'c': 3, 'd.e': 4}
# dict_list = [{'a': 1}, {'b': 2, 'c': 3}, {'d': {'e': 4}}]
# flattened = {}
# for d in dict_list:
#     tracker = [(d, "")]
#     while tracker:
#         current_d, key_prefix = tracker.pop()
#         for key, value in current_d.items():
#             if key_prefix:
#                 new_key = f"{key_prefix}.{key}"
#             else:
#                 new_key = key
#             if isinstance(value, dict):
#                 tracker.append((value, new_key))
#             else:
#                 flattened[new_key] = value
# print(flattened)

# 5. Diamond Star Pattern:
# Input: 5
# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
# rows = input("Enter a positive number: ")
# if rows.isdigit():
#     rows = int(rows)
# rows1 = int(rows) - 1
# for i in range(1, rows+1):
#     print(" "*rows + "*"*(i*2 - 1))
#     rows-=1
# for j in range(1, rows1+1):
#     print(" "*(j+1) + "*"*(rows1*2 - 1))
#     rows1-=1


# __SET 4__:

# 1. Simple Calculator using Operators:
# Input two integers and an operator (+,-,*,/). Perform operation.
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
# else:
#     print("Invalid input")
#     exit()
# op = input("Enter operator (+, -, *, /): ")
# result = 0
# if op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "*":
#     result = num1 * num2
# elif op == "/":
#     result = num1 / num2
# else:
#     print("Invalid Operator")
#     exit()
# print(f"{num1} {op} {num2} = {result}")

# 2. Float List: Avg>60 Check
# Input N floats. Calculate average and check if>60. Print True/False.
# input_string = input("Enter multiple float values with spaces: ")
# float_list = []
# for i in input_string.split():
#     float_list.append(float(i))
#
# average = sum(float_list) / len(float_list)
#
# print(average>60)

# 3. Login attempt limit with while loop:
# Give user 3 attempts to enter correct password. Lock account after 3 login attempts.
# password = "Admin@123"
# count = 3
# while count!=0:
#     pass_input = input("Username: Admin \nEnter your password: ")
#     if pass_input == password:
#         print("Login Successful!")
#         exit()
#     else:
#         count-=1
#         print(f"Invalid Password \nYou have {count} attempts left.")
# if count==0:
#     print("Account Locked!!")

# 4. Recursive Dictionary Flattener (Full)
# Input deeply nested dictionary and flatten all keys.
# # Example: {"a": {"b": {"c": 1}}, "x": 2} -> {'a.b.c': 1, 'x': 2)
# d = {"a": {"b": {"c": 1}}, "x": 2}
# flat_d = {}
# track = [(d, "")]
# while track:
#     current_d, key_prefix = track.pop()
#     for key, value in current_d.items():
#         if key_prefix:
#             new_key = f"{key_prefix}.{key}"
#         else:
#             new_key = key
#         if isinstance(value, dict):
#             track.append((value, new_key))
#         else:
#             flat_d[new_key] = value
#
# print(flat_d)

# 5. Pascal Triangle Full Pattern:
# Input = 5
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

# rows = 5
# for i in range(rows):
#     nu = 1
#     row = []
#     for j in range(i+1):
#         row.append(str(nu))
#         nu = nu * (i-j)//(j+1)
#     print(" ".join(row))


# __SET 5__:

# 1. Area calculator for Circle or Square:
# shape = input("Enter circle or square: ")
# if shape == "circle":
#     r = float(input("Enter radius: "))
#     print(f"Area of the circle with radius {r} is {3.14*r*r}")
# elif shape == "square":
#      a = float(input("Enter length of the side of a square: "))
#      print(f"Area of the square with side {a} is {a*a}")

# 2. List intersection without \
# Input two lists, print common elements without using set()
# l1 = [1, 2, 3, 4, 5]
# l2 = [2, 4, 6, 7, 8]
# l3 = []
# for i in l1:
#     if i in l2:
#         l3.append(i)
# print(l3)

# 3. Temperature alert system (Nested If)











