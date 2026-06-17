# key: value
# key must be unique, int, string
# value
# student_scores = {"mark": 89, "john": 34, "joseph": 66} 

# ### how to retrieve a value based on a key
# mark_score = student_scores["mark"] #89, Case-sensitive 
# print(mark_score)

# ### how to update the value based on key
# student_scores["john"] = 76
# print(student_scores)

# ### how to add a new key / value into dictionary
# student_scores["mary"] = 88
# print(student_scores)

# ### how to delete a key / pair from dictionary
# del student_scores["joseph"]
# print(student_scores)

# # ### how to check if something is is in the dictionary
# # check_student = input("Who do you want to check? ")
# # if check_student in student_scores:
# #     print(f"The score for {check_student} is {student_scores[check_student]}")
# # else:
# #     print(f"{check_student} is not in my class.")

# ### how to loop through dictionary
# for name in student_scores: # prints out the key
#     # print(name)
#     # print(student_scores[name])

#     print(f"{name} scored {student_scores[name]}")

# #### shortcut...
# for name, score in student_scores.items():
#     print(f"{name} scored {score}")





################ SET 1: Country and Capital ################

################ Define a dictionary ###############
# Define a dictionary named countries which will store a country and its capital city.

# 'Indonesia' has capital 'Jakarta'
# 'Malaysia' has capital 'Kuala Lumpur'
# 'Thailand' has capital 'Bangkok'
# 'Japan' has capital 'Tokyo'

# countries = {"Indonesia" : "Jakarta" , "Malaysia" : "Kuala Lumpur", "Thailand" : "Bangkok", "Japan" : "Tokyo"}
# print(countries)



################ Retrieve values from a dictionary ###############
# Print out the capital city of Malaysia only.
# Print out the capital city of Japan only.

# msia_city = countries["Malaysia"]
# print(msia_city)
# jpn_city = countries["Japan"]
# print(jpn_city)

########### Change the value of a dictionary key ###############
# Change the capital city of Thailand to 'Phuket'.
# Change the capital city of Indonesia to 'Bali'.

# countries["Thailand"] = "Phuket"
# countries["Indonesia"] = "Bali"
# print(countries)

############ Add a new key / value to the dictionary #####################
# Add a new country => China with capital Beijing.
# Add a new country => South Korea with capital Seoul.

# countries["China"] = "Beijing"
# countries["South Korea"] = "Seoul"
# print(countries)

############ Delete a key / value from the dictionary #####################
# Delete the country Indonesia from the dictionary.

# del countries["Indonesia"]
# print(countries)


########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each country.
# Only display the keys.

# for country, capital in countries.items():
#     print(country)


########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the capital cities.

# for country, capital in countries.items():
#     print(capital)


########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the country and its capital city.

# Example:
# Malaysia has capital city Kuala Lumpur
# Japan has capital city Tokyo

# for country, capital in countries.items():
#     print(f"{country} has capital city {capital}")


################ SET 2: Student and Marks ################

################ Define a dictionary ###############
# Define a dictionary named marks which will store a student name and the marks they scored.

# 'Alice' scored 78
# 'Ben' scored 64
# 'Chloe' scored 89
# 'Daniel' scored 55

# write and test your code here

# marks = {"Alice" : 78, "Ben" : 64, "Chloe" : 89, "Daniel" : 55}
# print(marks)


################ Retrieve values from a dictionary ###############
# Print out the marks scored by Alice only.
# Print out the marks scored by Daniel only.

# alice_marks = marks["Alice"]
# print(alice_marks)

# daniel_marks = marks["Daniel"]
# print(daniel_marks)

########### Change the value of a dictionary key ###############
# Change Ben's marks to 70.
# Change Daniel's marks to 60.

# marks["Ben"] = 70
# marks["Daniel"] = 60
# print(marks)


############ Increase the value of a dictionary key ############
# Increase Chloe's marks by 5.
# Decrease Alice's marks by 3.

# chloe_marks = marks["Chloe"]
# new_chloe_marks = chloe_marks + 5
# marks["Chloe"] = new_chloe_marks

# # TC:
# # marks["Chloe"] = marks["Chloe"] + 5

# marks["Alice"] -= 3

# print(marks)

############ Add a new key / value to the dictionary #####################
# Add a new student => Ethan who scored 82.
# Add a new student => Fiona who scored 91.

# marks["Ethan"] = 82
# marks["Fiona"] = 91
# print(marks)

############ Delete a key / value from the dictionary #####################
# Delete Daniel from the dictionary.

# del marks["Daniel"]
# print(marks)


########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each student.
# Only display the keys.

# for name, score in marks.items():
#     print(name)

########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the marks.

# for name, score in marks.items():
#     print(score)

########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the student name and marks.

# Example:
# Alice scored 78 marks
# Ben scored 64 marks

# write and test your code here

# for name, score in marks.items():
#     print(f"{name} scored {score} marks")

################ SET 3: Game Item and Quantity ################

################ Define a dictionary ###############
# Define a dictionary named inventory which will store a game item 
# and the quantity owned by the player.

# 'potion' quantity is 5
# 'sword' quantity is 1
# 'shield' quantity is 1
# 'arrow' quantity is 20

inventory = {"potion" : 5, "sword" : 1, "shield" : 1, "arrow" : 20}
print(inventory)

################ Retrieve values from a dictionary ###############
# Print out the quantity of potion only.
# Print out the quantity of arrow only.

# potion_quan = inventory["potion"]
# print(potion_quan)
# arrow_quan = inventory["arrow"]
# print(arrow_quan)

########### Change the value of a dictionary key ###############
# Change the quantity of sword to 2.
# Change the quantity of shield to 3.

# inventory["sword"] = 2
# inventory["shield"] = 3
# print(inventory)

############ Increase the value of a dictionary key ############
# Increase the quantity of potion by 10.
# Decrease the quantity of arrow by 5.

# inventory["potion"] += 10
# inventory["arrow"] -= 5
# print(inventory)


############ Add a new key / value to the dictionary #####################
# Add a new item => bow with quantity 1.
# Add a new item => apple with quantity 8.

# inventory["bow"] = 1
# inventory["apple"] = 8
# print(inventory)

############ Delete a key / value from the dictionary #####################
# Delete apple from the dictionary.

# del inventory["apple"]
# print(inventory)


########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of each item.

# Only display the keys.

# for name, quan in inventory.items():
#     print(name)

########### Loop through to Retrieve Values ##################
# Write a for loop, and only print out the quantities.
# '''

# # write and test your code here

# for name, quan in inventory.items():
#     print(quan)

########### Loop through to Retrieve Key and Values ##################
# Write a for loop, and print out the item and quantity.

# Example:
# potion quantity: 5
# arrow quantity: 20


# write and test your code here

# for name, quan in inventory.items():
#     print(f"{name} quantity: {quan}")
