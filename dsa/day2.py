# 1. CODING PROBLEM
# FIND THE SECOND LARGEST UNIQUE NUMBER
#
# My Approach:
# I will traverse the list and keep track of two values:
# largest and second_largest.
#
# I will handle duplicate values by checking whether the
# current number is different from the largest value.
#
# I will not sort the list.
#
# If there is no second largest unique number, I will print
# "No second largest number".
#
# My Code:
#


numbers = [10, 5, 8, 20, 15]

largest = None
second_largest = None

for number in numbers:

    if largest is None or number > largest:
        second_largest = largest
        largest = number

    elif number != largest and (
        second_largest is None or number > second_largest
    ):
        second_largest = number

if second_largest is None:
    print("No second largest number")
else:
    print("Second largest:", second_largest)


# Test Case 1

#
# Input: [10, 5, 8, 20, 15]
# Expected Output: 15
#
# Actual Output:
# Second largest: 15

# Test Case 2

#
# Input: [10, 20, 20, 8, 15]
# Expected Output: 15
#
# Actual Output:
# Second largest: 15
#

# Test Case 3

#
# Input: [5, 5, 5]
# Expected Output: No second largest number
#
# Actual Output:
# No second largest number
#

# Bonus Challenge - One Pass

# The above solution already solves the problem in one pass.
#
# During the traversal, we keep track of only two values:
#
# 1. largest
# 2. second_largest
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
#

# 2. CONCEPT QUESTION
# MUTABLE VS IMMUTABLE
#
#
# What is mutable vs immutable?
#
# Mutable objects can be changed after they are created.
# Immutable objects cannot be changed after they are created.
#
# Mutable:
# list
# set
# dictionary
#
# Immutable:
# int
# float
# string
# tuple
#
# Examples:
#
# List:
# numbers = [10, 20, 30]
# numbers.append(40)
#
# Tuple:
# numbers = (10, 20, 30)
#
# String:
# name = "Sathwik"
#
# Set:
# numbers = {10, 20, 30}
#
# Dictionary:
# student = {"name": "Sathwik", "age": 21}
#
#
#
# Interview Follow-up Answers

#
# Given:
#
# a = [10, 20, 30]
# b = a
# b.append(40)
#
# Q1. What will be the output?
#
# [10, 20, 30, 40]
# [10, 20, 30, 40]
#
# Q2. Why did changing b also change a?
#
# Because b = a does not create a new list.
# Both variables refer to the same list object in memory.
#
# Therefore, when we modify b, the same list referenced by
# a is also modified.
#
# Q3. How would you create an independent copy of a?
#
# We can use:
#
# b = a.copy()
#
# or:
#
# b = a[:]
#
#

# 3. DEBUGGING CHALLENGE
#
# Original code:
#
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for i in range(1, len(numbers)):
#     total = total + numbers[i]
# print("Total:", total)
#
# What was the error?
#
# The range starts from 1 instead of 0.
#
# Therefore, the first element, numbers[0], which is 10,
# is skipped.
#
# Why did it happen?
#
# range(1, len(numbers)) starts the loop from index 1.
#
# The indexes of the list are:
#
# 0 -> 10
# 1 -> 20
# 2 -> 30
# 3 -> 40
# 4 -> 50
#
# Because the loop starts at index 1, 10 is not added.
#
# My corrected code:
#


numbers = [10, 20, 30, 40, 50]

total = 0

for i in range(len(numbers)):
    total = total + numbers[i]

print("Total:", total)


# Expected Output:
# Total: 150
#
#
# Test with another list:
#


numbers = [5, 10, 15, 20]

total = 0

for i in range(len(numbers)):
    total = total + numbers[i]

print("Total:", total)


# Output:
# Total: 50
#
#

# Debugging 
# Without using range(len(numbers))
# 
#


numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total = total + number

print("Total:", total)


# Output:
# Total: 150
#
#

# 4. MINI INTERVIEW

#
# Q1. What is the difference between = and == in Python?
#
# = is the assignment operator.
# It is used to assign a value to a variable.
#
# Example:
# x = 10
#
# == is the comparison operator.
# It checks whether two values are equal.
#
# Example:
# x == 10
#
#
# Q2. What is the difference between break and continue?
#
# break completely stops the loop.
#
# continue skips the current iteration and moves to the
# next iteration.
#
# Example:
#
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
#
# Output:
# 0
# 1
# 2
#
#
# Example of continue:
#
# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
#
# Output:
# 0
# 1
# 2
# 4
#
#
# Q3. What happens when you execute:
#
# numbers = [1, 2, 3]
# numbers.append(4)
#
# The value 4 is added to the end of the list.
#
# Result:
# [1, 2, 3, 4]
#
#
# Q4. What is the difference between append(10) and
# extend([10, 20])?
#
# append() adds one item to the list.
#
# Example:
# numbers = [1, 2, 3]
# numbers.append(10)
#
# Result:
# [1, 2, 3, 10]
#
# extend() adds multiple elements from another iterable.
#
# Example:
# numbers = [1, 2, 3]
# numbers.extend([10, 20])
#
# Result:
# [1, 2, 3, 10, 20]
