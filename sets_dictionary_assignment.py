# Q1. Create a dictionary named student_info with the following keys:
#       student_name, age, roll_no, class, section, percentage, college_name.
#           a) Print all the keys and values from the dictionary.
#           b) Add a new key-value pair: 'email': 'student@example.com' to the dictionary.
#           c) Delete the section key from the dictionary.
#           d) Use a loop to print all key-value pairs in the dictionary in the format: Key --> Value
#           e) Check if the key 'college_name' exists in the dictionary or not.

student_info = {"student_name": "Harry",
                "age": 20,
                "roll_no": 201,
                "class": "Python Programming",
                "section": "A",
                "percentage": 85.5,
                "college_name": "UST University"}

# a) Print all the keys and values from the dictionary.
print(f"All keys: {student_info.keys()}")
print(f"All values: {student_info.values()}")

# b) Add a new key-value pair: 'email': '
student_info.update({'email': 'harry@email.com'})
print(f"After adding 'email': {student_info}")

# c) Delete the section key from the dictionary.
student_info.pop('section')
print(f"After deleting 'section': {student_info}")

# d) Use a loop to print all key-value pairs in the dictionary in the format: Key --> Value
for key, value in student_info.items():
    print(f"{key} --> {value}")

# e) Check if the key 'college_name' exists in the dictionary or not.
if 'college_name' in student_info.keys():
    print("'college_name' exists in the student_info dictionary.")
else:
    print("'college_name' does not exist in the student_info dictionary.")

print()
print()

# Q2. You are given three sets representing students enrolled in different courses:
python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "Eve", "Frank", "David"}
cpp_students = {"Charlie", "George", "Eve", "Henry"}

# Find students who are enrolled in all three courses.
all_three = python_students & java_students & cpp_students
if not all_three:
    print("No students are enrolled in all three courses.")
else:
    print(f"Students enrolled in all three courses: {all_three}")

# Find students who are enrolled in only Python course.
only_python = python_students - (java_students | cpp_students)
print(f"Students enrolled only in Python course: {only_python}")

# Find students who are enrolled in both Python and Java.
python_and_java = python_students & java_students
print(f"Students enrolled in both Python and Java courses: {python_and_java}")

# Find students who are enrolled in either Python or Java but not both.
either_python_or_java = python_students.symmetric_difference(java_students)
print(f"Students enrolled in either Python or Java but not both: {either_python_or_java}")

# Find the list of all unique students enrolled in any course.
unique_all_courses = python_students | java_students | cpp_students
print(f"List of students from all courses: {unique_all_courses}")

# Find students who are in Java or C++, but not in Python.
java_cpp_not_python = (java_students | cpp_students) - python_students
print(f"Students enrolled in Java or C++ but not in Python: {java_cpp_not_python}")

# Check if all Python students are also Java students.
print(f"Are all Python students also Java students?: {python_students.issubset(java_students)}")

# Add a new student "Jones" to the Python set.
python_students.add("Jones")
print(f"Python students after adding 'Jones': {python_students}")

# Remove "Frank" from the Java set.
java_students.remove("Frank")
print(f"Java students after removing 'Frank': {java_students}")

# Clear the cpp_students set.
cpp_students.clear()
print(cpp_students)
