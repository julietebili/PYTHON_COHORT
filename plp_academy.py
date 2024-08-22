# # # favorite number
# # favorite_Number = 55
# # print(f'My favourite number is {favorite_Number}')
# # #String
# # greeting = 'Hello PLP!'
# # print(greeting)
# # #Boolean
# # is_python_fun = True
# # is_python_boring = False
# # print(f"Is python fun? {is_python_fun}")
# # print(f'Is python boring? {is_python_boring}')

# # # Control Flow
# # speed = 80
# # if speed > 70:
# #     print("Fast")
# # if speed > 40:
# #         print("Safe")
# # else:
# #      print("slow")

# # #Loops for $ while
# # for i in range(8):
# #     print(f'I love PLP Academy {i}')

# # CountDown = 10
# # while CountDown > 0:
# #     print(f'The Count is: {CountDown}')
# #     CountDown -= 1
# # print("Count Down Successful!!!")

# #DEfine A Function
# # def greet(person):
# #     return f"Good Afternoon, {person}"
# # #Apply the Function
# # print(greet("Juliet"))
# # print(greet("Jane"))

# #Lists and Dictionaries
# fruits_list = ["Apple", "Cherry", "Mango"]
# fruits_tuple = ("Bnana", "Pineapple", "Orange")
# print(fruits_list)
# print(fruits_tuple)

# #Dictionary
# Contacts = {
# #     "Alice": "33220799",
# #     "John": "34350520",
# #     "Mark": "60000760"
# # }
# # print(f"Mark contact is {Contacts['Mark']}")

# # # #Inbuilt modules
# # # #Modules
# import math
# # use a function from module math
# result = math.sqrt(49)
# print(f'The square root of 49 is {result}')

# # #customized module
# import greet_module
# print(greet_module.greet("Jane"))

# ## Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
# integer_list = ["10,20,20,30,40"]
# print(integer_list)

# # # Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
# # favorite_books = ("ArcAngel", "Roses and Roses", "TheMandate", "TheAngel", "TheShadow")
# # # Iterate over the tuple and print each book name on a separate line
# # for book in favorite_books:
# #     print(book)

# # # Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# # Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

# # create information to store 
# person = {}

# #ask the user for their name
# name = input("What is your name?")

# #ask the user for their age
# age = input("How old are you?")

# #Ask the user for their favorite color
# favorite_color = input("What is your favorite color?")

# #store information in dictionary
# person["name"] = name
# person["age"] = age
# person["favorite_color"] = favorite_color

# #print the dictionary to the console
# print(person)

# Write a program that accepts user input to create two sets of integers. 
# Function to create a set from user input
# def create_set(set_number):
#     print(f"Enter integers for Set {set_number} separated by spaces:")
#     user_input = input()  # Take input from the user
#     # Split the input by spaces and convert each part to an integer, then create a set
#     integer_set = set(map(int, user_input.split()))
#     return integer_set

# # Create two sets using user input
# set1 = create_set(1)
# set2 = create_set(2)

# # Display the sets
# print(f"\nSet 1: {set1}")
# print(f"Set 2: {set2}")

# Then, create a new set that contains only the elements that are common to both sets.
# Function to create a set from user input
def create_set(set_number):
    print(f"Enter integers for Set {set_number} separated by spaces:")
    user_input = input()  # Take input from the user
    # Split the input by spaces and convert each part to an integer, then create a set
    integer_set = set(map(int, user_input.split()))
    return integer_set

# Create two sets using user input
set1 = create_set(1)
set2 = create_set(2)

# Find the intersection (common elements) of the two sets
common_set = set1.intersection(set2)

# Display the sets and the common elements
print(f"\nSet 1: {set1}")
print(f"Set 2: {set2}")
print(f"Common elements: {common_set}")

