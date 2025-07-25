# Q1. Create list called "even", store all the even numbers, in the range of 1 to 20.

even = []
for i in range(1, 21):
    if i%2 == 0:
        even.append(i)
print(f"Even = {even}")

# Q2. Create list called "odd", store all the odd numbers, int the range of 1,20.

odd = []
for i in range(1, 21):
    if i%2 != 0:
        odd.append(i)
print(f"Odd = {odd}")

# Q3. Take "even" and "odd" list  from previous solution, merge it in new list called "numbers" and sort it.

numbers = even+odd
numbers.sort()
print(f"Numbers = {numbers}")


# Q4. Create a nested list for called "Students" for 5 student, each index store the student information. ex.. ["name",roll,marks].

students = [["Harry", 101, 92.0], ["Ron", 102, 86.5], ["Hermione", 103, 99.0], ["Neville", 104, 82.0], ["Draco", 105, 74.5]]
print(f"List of Students: {students}")

# Q5. Write a Python program to find the second-largest number in a list.

numbers_list = [10, 38, 8, 45, 64, 99, 67, 101]
print(f"Numbers list: {numbers_list}")
numbers_list.sort()
print(f"Second Largest number in numbers list is: {numbers_list[-2]}")

# Q6. WAP to print unique element from list.
#      ex... nums = [4,3,5,6,3,4,6]      (o/p:- 5 is unique from list)

nums = [4,3,5,6,3,4,6]
unique_list =[]
for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1
    if count == 1:
        unique_list.append(i)
print(f"{unique_list} is unique from list")

# Q7. Given a tuple of numbers, find the max and min elements.
#   ex. tup = (11,26,45,23,15,18)

tup = (11,26,45,23,15,18)
print(f"Max number from tuple: {max(tup)}")
print(f"Min number from tuple: {min(tup)}")

# Q8. Retrieve the 'G' from following list using positive indexing
#        L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]

L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
print(L1[3][2][2][1][1])

# Q9. WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
#        L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]

L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

# Q10. WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
#       s2 = 'Hello I am going to Bengaluru How are you doing?'

s2 = 'Hello I am going to Bengaluru How are you doing?'
print(s2[-20:-30:-1])
print(s2[-28:-19:1])



