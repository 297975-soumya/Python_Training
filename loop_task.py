# 1. Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i, end=" ")

print()

j = 0
while j < 11:
    print(j, end=" ")
    j+=1

print()

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i, end=" ")

print()

j = 10
while j >= 0:
    print(j, end=" ")
    j-=1

print()

# 3. Write a loop that makes seven calls to print(), so we get on the output the following (8X8 #)
count = 1
while count<=8:
    print("# "*8)
    count+=1

# 4. Use nested loops to create the following (pyramid)
num = int(input("enter a number (preferably 13): "))

for i in range(1, num+1, 2):
    print(" "*num+"# "*i)
    num -= 2

# 5. Print the following pattern using loops (0 X 0 = 0 ..... 10 X 10 = 100
for i in range(11):
    print(f"{i} X {i} = {i**2}")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Scikit', 'Pytorch'] using a for loop and print out the items.
my_list = ['Python', 'Numpy','Pandas','Scikit', 'Pytorch']

for i in my_list:
    print(i)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(1, 101):
    if i%2 == 0:
        print(i, end=" ")

print()

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(1, 101):
    if i%2 != 0:
        print(i, end=" ")

print()

# 9. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
result = 0
for i in range(0, 101):
    result += i
print(result)

# 10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
odd_sum = 0
even_sum = 0
for i in range(1, 101):
    if i%2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of all odds from 0 to 100: {odd_sum}")
print(f"Sum of all evens from 0 to 100: {even_sum}")


