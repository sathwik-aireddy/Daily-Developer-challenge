# DAILY DEVELOPER CHALLENGE - DAY 1
# Name: Sathwik Aireddy
# Day: 1
#

# 1. CODING PROBLEM - FIRST NON-REPEATING CHARACTER

#
# Approach:
# Take a string as input.
# Use a dictionary to count the frequency of each character.
# Ignore spaces.
# Traverse the string again and find the first character
# whose frequency is 1.
# If no such character is found, print the required message.
#
# Code:

text = input("Enter a string: ")

frequency = {}

for char in text:
    # Ignore spaces
    if char == " ":
        continue

    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

found = False

for char in text:
    # Ignore spaces
    if char == " ":
        continue

    if frequency[char] == 1:
        print("First non-repeating character:", char)
        found = True
        break

if not found:
    print("No non-repeating character found")

#
# Test Inputs:
#
# Input: programming
# Output: First non-repeating character: p
#
# Input: aabbcdd
# Output: First non-repeating character: c
#
# Input: aabbcc
# Output: No non-repeating character found
#
# Input: a a b b c
# Output: First non-repeating character: c
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#

# 2. CONCEPT QUESTION - PYTHON DATA STRUCTURES


#
# List[]
# Ordered, allows duplicates, and is mutable.
# Example: [10, 20, 10]
#
# Tuple()
# Ordered, allows duplicates, and is immutable.
# Example: (10, 20, 10)
#
# Set{}
# Stores unique values and is mutable.
# Example: {10, 20, 30}
#
# Dictionary{}
# Stores data as key-value pairs and is mutable.
# Dictionary keys cannot be duplicated.
# Example: {"name": "Sathwik", "age": 21}
#
# Interview Follow-up:
#
# 1. For storing unique student IDs, I would use a set
# because a set does not allow duplicate values.
#
# 2. For storing a student's name, email, and phone number,
# I would use a dictionary because it stores data using
# meaningful key-value pairs.
#

# 3. DEBUGGING CHALLENGE

#
# What was the issue?
#
# The "else" statement was executed for every student who
# was not Kiran. Therefore, "Student not found" was printed
# multiple times.
#
# How did you fix it?
#
# I used a found variable to keep track of whether Kiran
# was found. When Kiran is found, the program prints the
# result and stops the loop using break.
#
# After checking the list, if found is still False,
# the program prints "Student not found".

# Corrected Code:

students = ["Ravi", "Anil", "Kiran", "Suresh"]

found = False

for student in students:
    if student == "Kiran":
        print("Student found:", student)
        found = True
        break

if not found:
    print("Student not found")

#

# The problem can also be solved without range(len(students))
# by directly checking whether "Kiran" exists in the list.
#

if "Kiran" in students:
    print("Student found: Kiran")
else:
    print("Student not found")



# 4. WHAT I LEARNED TODAY:


# I learned how to use a dictionary to count character
# frequency and find the first non-repeating character.
#
# I also learned the differences between list, tuple,
# set, and dictionary.
#
# I learned how an incorrectly placed else statement can
# produce unwanted output.
#
# I also learned how to use a flag variable and break
# to control a loop.
#

# 5. WHAT I FOUND DIFFICULT:

#
# I found the debugging challenge slightly difficult because
# "Student not found" was printed multiple times.
#
# I understood that the complete list should be checked
# before deciding that Kiran is not present.
#
# I also found the first non-repeating character problem
# useful for understanding dictionaries and frequency counting.