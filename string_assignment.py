
# Conceptual Questions:

# Explain the difference between immutable and mutable types in Python. How does this apply to strings?
"""
In Python language, data types can be either mutable or immutable. Those data types that can be changed or modified
after creation are mutable types, and those data types that cannot be changed or modified after creation are immutable
types. Strings are immutable types in Python.
"""

# Describe the role of escape characters in Python strings. Give examples.
"""
To represent strings, single quotes or double quotes are used in Python. However, if these quotes are a part
of the string itself, then the compiler might get confused about the start and end of the string. For clarity, escape
characters are used. An escape character is a backslash (\\) followed by a character that has a special meaning like a
quotes, a newline, including a backslash itself as part of the string.
"""


# Coding Questions:

# Write a Python program that takes a string and removes all vowels.
str1 = "Hello World"
vowels = "aeiou"
for char in str1:
    if char.lower() in vowels:
        str1 = str1.replace(char,"")
print(str1)

# Given a string, write a program to count the frequency of each character.
str2 = "Mississippi"
char_count = {}
for char in str2:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# Write a Python program to check if two given strings are anagrams of each other
word1 = "Listen"
word2 = "Silent"
a = list(word1.lower())
b = list(word2.lower())
a.sort()
b.sort()
if a == b:
    print(f"{word1} and {word2} are anagrams of each other.")
else:
    print(f"{word1} and {word2} are not anagrams of each other.")

# Write code to reverse the order of words in a sentence, without using built-in reverse functions
str3 = "This is a test string"
word_list = str3.split()
str3 = " ".join(word_list[::-1])
print(str3)

# Write a Python program to find the longest substring without repeating characters.
str4 = "Let us find the longest substring"
substrings = str4.split()
longest_substring = ""
for substring in substrings:
    if len(set(substring)) > len(longest_substring):
        longest_substring = substring
print(f"The longest substring in the given string without repeating characters is: {longest_substring}")

# Write a program to check if a string is a palindrome, ignoring spaces and punctuation.
input_string = "A man, a plan, a canal – Panama!"
check_list = []
for char in input_string.lower():
    if char.isalpha():
        check_list.append(char)

if check_list == check_list[::-1]:
    print(f"{input_string} is a palindrome")
else:
    print(f"{input_string} is not a palindrome")

# Write code to convert a string so that the first letter of each word is capitalized (like title case), without using Title()
str4 = "this is a Test string"
words = str4.split()
capitalized_words = [word.capitalize() for word in words]
str4 = " ".join(capitalized_words)
print(str4)



