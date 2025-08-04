
# Create an empty dictionary called bird
bird = {}

# Add name, color, breed, legs, age to the bird dictionary
bird["name"] = "Bald Eagle"
bird["colour"] = "Brown with white head and tail"
bird["breed"] = "Eagles"
bird["legs"] = 2
bird["age"] = 10

print(bird)

# Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
student = {"first_name": "Harry", "last_name": "Potter", "gender": "Male", "age": 28, "marital_status": "Single",
           "skills": ["Python", "Java", "C++"], "country": "India", "city": "Bangalore",
           "address": "9, Magic Street, Bangalore, India"}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
skills = student.get("skills")
print(skills)
print(type(skills))

# Modify the skills values by adding one or two skills
skills.extend(["Azure", "DevOps"])
print(student["skills"])

# Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)

# Get the dictionary values as a list
values_list = list(student.values())
print(values_list)

# Change the dictionary to a list of tuples using items() method
dict_items = list(tuple(student.items()))
print(dict_items)

# Delete one of the items in the dictionary
student.popitem()
print(student)

# Delete one of the dictionaries
del bird
