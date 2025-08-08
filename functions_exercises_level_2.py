# Exercises ➞ Level 2:

# 1. Declare a function named evens_and_odds.
# It takes a positive integer as parameter, and it counts number of evens and odds in the number.

def evens_and_odds(num: int):
    even_count = 0
    odd_count = 0
    while num:
        last_digit = num % 10
        if last_digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num //= 10
    return even_count, odd_count

num_input = int(input("Enter a positive integer: "))
even, odd = evens_and_odds(num_input)
print(f"For integer: {num_input}, Even digits count: {even}, Odd digits count: {odd}")


# 2. Call your function factorial,
# it takes a whole number as a parameter, and it returns a factorial of the number

def factorial(num: int):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result
input_num = int(input("Enter a positive integer: "))
print(f"Factorial of {input_num} is {factorial(input_num)}")

# 3. Call your function is_empty, it takes a parameter, and it checks if it is empty or not

def is_empty(para):
    return True if len(para) == 0 else False

empty_para = []
if is_empty(empty_para):
    print(f"Input parameter {type(empty_para).__name__} is empty")
else:
    print(f"Input parameter {type(empty_para).__name__} is not empty")

# 4. Write different functions which take lists.
# They should calculate_mean, calculate_median, calculate_mode, calculate_range,
# calculate_variance, calculate_std (standard deviation)

def calculate_mean(data):
    mean = sum(data) / len(data)
    return mean

def calculate_median(data):
    sorted_data = sorted(data)
    if len(sorted_data) % 2 != 0:
        median = sorted_data[len(data) // 2]
    else:
        median = ((sorted_data[(len(data) // 2) - 1]) + sorted_data[len(data) // 2]) / 2
    return median

def calculate_mode(data):
    '''
    mode: the one value which repeats most number of times
    or
    the two values that repeat most number of times (multimodal)
    or
    if there are no repeating values then there is no mode
    '''

    pass

def calculate_range(data):
    sorted_data = sorted(data)
    data_range = sorted_data[-1] - sorted_data[0]
    return data_range

def calculate_variance(data):
    mean = calculate_mean(data)
    squared_differences = []
    for n in data:
        squared_differences.append((n - mean) ** 2)
    variance = sum(squared_differences) / (len(data) - 1)
    return variance

def calculate_std(data):
    var = calculate_variance(data)
    std = var ** 0.5
    return std

data_list = [10, 20, 85, 45, 36, 18, 94, 108, 134, 9]

print(f"Input data: {data_list}")
print(f"Mean: {calculate_mean(data_list)}, Median: {calculate_median(data_list)}, "
      f"Mode: {calculate_mode(data_list)}, Range: {calculate_range(data_list)}, "
      f"Variance: {calculate_variance(data_list)}, Standard Deviation: {calculate_std(data_list)}")
