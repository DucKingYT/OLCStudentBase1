# Slicing >>> retrieve sub-parts of a string, list variable

# word = "SINGAPORE"

# #### retrieve the first character
# char = word[0]  ## S
# print(char)

# #### retrieve the last character ???
# last = word[-1] # retrieves E
# print(last)

# ### SING
# print(word[:4]) 

# # SLICING [start : stop : step]  ### very much like the range()

# ### GAP
# print(word[3:6])

# ### ORE
# print(word[6:])

# #### last 3 character of word
# word1  = "SINGAPORELANDISTHEBESTCOUNTRYINTHEWORLD"
# print(word1[-3:])

# ## retrieve every second character
# print(word1[::2])

# ## reverse the word
# reverse = word1[::-1]
# print(reverse)

# ## PALINDROME eg: HANNAH, RACECAR, BOB, LOL
# if word1 == word1[::-1]:
#     print(f"{word1} is a palindrome")
# else:
#      print(f"{word1} is not a palindrome")

#### Write a program to generate a username
### Ask for the first name, change to upper case
### Ask for the last name, change to upper case
### Use the first 3 characters from firstname and last 3 characters from lastname
### append a random number from 100 to 999 at the end 
## eg:
### KEVIN
### TONG
### KEVONG552

# import random

# first_name = input("Enter your first name: ")
# new_first_name = first_name.upper() 
# last_name = input("Enter your last name: ")
# new_last_name = last_name.upper() 

# first_3 = new_first_name[:3]
# last_3 = new_last_name[-3:]

# rand_num = random.randint(100, 999)

# username = f"{first_3}{last_3}{rand_num}"

# print(f"Welcome, {username}")

# # String and List Operators
# # Using + to Concatenate
# # List Slicing

# '''
# Question 1: Extract a portion of a list and creates a new list
# that contains only the first three elements of the original list.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [1, 2, 3]
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[:3] # from start, up to 3 but not including 3
# print(newlist) # returns [1,2,3]







# '''
# Question 2: Get the last three items of a list.
# Ask the user for a list of numbers and print the last three items.
# Example Input: [10, 20, 30, 40, 50]
# Example Output: [30, 40, 50]
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[-3:] # from last 3rd, to the end
# print(newlist) # returns [3,4,5]







# '''
# Question 3: Create a sub-list from a list using slicing.
# Given a list of elements, write a function that returns a
# sublist from the second element to the second last element.
# Example Input: [0, 1, 2, 3, 4, 5]
# Example Output: [1, 2, 3, 4]
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[1:-1] # from the second element to the second last element
# print(newlist) # returns [2,3,4]






# '''
# Question 4: Reverse a list using slicing.
# Write a function that takes a list and returns it reversed.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5]
# newlist = inlist[::-1] # reverse it
# print(newlist) # returns [5,4,3,2,1]







# '''
# Question 5: Slice a list into halves.
# Divide a list into two equal halves and returns both halves.
# You may assume that the list has an even number of items
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 2, 3]  [4, 5, 6]
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# listlen = len(inlist) # find length of list
# midindex = listlen // 2 # find the middle index / position
# first_half = inlist[:midindex]
# second_half = inlist[midindex:]
# print(first_half) # returns [1, 2, 3]
# print(second_half) # returns [4, 5, 6]





# '''
# Question 6: Extract every second element from a list.
# Write a function that returns a list of every second element from the given list.
# Example Input: ['a', 'b', 'c', 'd', 'e', 'f']
# Example Output: ['b', 'd', 'f']
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# newlist = inlist[1::2] # start from 1 (2nd place, to end, increments of 2)
# print(newlist) # returns [2,4,6]






# '''
# Question 7: Remove the first and last elements of a list using slicing.
# Create a function that takes a list and returns it without
# the first and last elements.
# Example Input: [0, 1, 2, 3, 4]
# Example Output: [1, 2, 3]
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# newlist = inlist[1:-1]
# print(newlist) # returns [2, 3, 4, 5]






# '''
# Question 8: Create code to reverse the order of elements in a
# list only from the second to the last but one.
# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [1, 5, 4, 3, 2, 6]
# '''
# ## Write and test your code here
# inlist = [1, 2, 3, 4, 5, 6]
# second_to_last = inlist[1:-1] # get 2nd to last
# reversed_middle = second_to_last[::-1] # reverse 2nd to last
# liststart = [inlist[0]] # retrieves 1st char and converts to list
# listend = [inlist[-1]] # retrieve last char and convert to list
# newlist = liststart + reversed_middle + listend
# print(newlist) # returns [1, 5, 4, 3, 2, 6]


# '''
# # Question 9: Extract the first three characters from a string
# # Test case 1: example input: hello, example output: hel
# # Test case 2: example input: Python, example output: Pyt
# '''
# ## Write and test your code here

# string1 = input("Enter a word: ")
# string2 = input("Enter a word again: ")

# string1_first3 = string1[:3]
# string2_first3 = string2[:3]

# print(string1, string2)
# print(string1_first3, string2_first3)


# '''
# # Question 10: Extract the last three characters from a string
# # Test case 1: example input: hello, example output: llo
# # Test case 2: example input: Python, example output: hon
# '''
# ## Write and test your code here





# '''
# # Question 11: Extract a subset of a list from index 2 to 5
# # Test case 1: example input: 1 2 3 4 5 6 7, 
# example output: [3, 4, 5, 6]
# # Test case 2: example input: 10 20 30 40 50 60, 
# example output: [30, 40, 50]
# '''
# ## Write and test your code here


# '''
# # Question 12: Extract every second character from a string
# # Test case 1: example input: hello, example output: hlo
# # Test case 2: example input: Python, example output: Pto
# '''
# ## Write and test your code here



# '''
# # Question 13: 
# # Write a function called mid3(instring)
# # Extract the middle three characters from a string
# # Check that the incoming string must be an odd length, 
# # Test case 1: example input: abcdefg, example output: cde
# # Test case 2: example input: helloworld, example output: Invalid, Even length
# '''
# ## Write and test your code here


# '''
# # Question 14: Extract the first half of a string
# # Test case 1: example input: hello, example output: hel
# # Test case 2: example input: Python, example output: Pyt
# '''
# ## Write and test your code here


# '''
# # Question 15: Extract the second half of a string
# # Test case 1: example input: hello, example output: llo
# # Test case 2: example input: Python, example output: hon
# '''
# ## Write and test your code here





# '''
# # Challenge 1:
# Write a program to 
# validate if a given input is a valid Singapore NRIC number. 
# A valid NRIC must start with 'S', 'T', 'F', or 'G', followed by 7 digits, 
# and ends with an uppercase letter.

# * In this case, assume that as long as the last character 
# is an uppercase letter it is valid.

# Normal Test: Input: "S1234567D", Output: True
# Error Test: Input: "A1234567D", Output: False
# Boundary Test: Input: "S123456", Output: False
# '''
# ## Write and test your code here

NRIC = input("Enter your NRIC: ")
validation = True

if not(NRIC[0] == "S" or NRIC[0] == "T" or NRIC[0] == "F" or NRIC[0] == "G"):
    validation = False
elif not(NRIC[1:8].isdigit()):
    validation = False
elif not(NRIC[-1].isalpha() and NRIC[8].isupper()):
    validation = False
if validation == True:
    print(f"Your NRIC, {NRIC} is accepted")
else:
    print(f"Your NRIC, {NRIC} is not accepted")
