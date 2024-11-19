#CONDITIONS and ELSE AND IF SCENARIOS
#simple password programme
# password = "passme"
# userinput = input("what is the password? ")
# if userinput == password:
#     print("Password is correct!!!")
# else:
#     print("Password is incorrect!!!")

################################################
#Grading System
# score = int(input("What is your score? "))
# if score >= 75:
#     print("your grade is A1")
# elif score >= 70:
#     print("Your grade is A2")
# elif score >= 65:
#     print("Your grade is B3")
# elif score >= 60:
#     print("Your score is B4")
# elif score >= 55:
#     print("your score is C5")
#################################
#Shopping and discout program
# Pens = int(input("How many pens do you want to buy? "))
# if Pens >= 100:
#     print("your total cost is",Pens*5 * 0.9)
# else:
#     print("your total cost is",Pens*5)
############################
#a little wrong but fixable
# import random
# rannum = random.randint(1, 101)
# print(rannum)
# for i in range(7):
#     input = int(input("Put in a number 1-100 "))
#     if input == rannum:
#         print("You are correct")
#         break #break out of a loop
#     elif input < rannum:
#         print("The number is bigger")
#     elif input > rannum:
#         print("The number is smaller")
# else:
#     print("You got it wrong 7 times,the number was",rannum)
########################################
# or statements
# anim1 = input("enter an animal ")
# anim2 = input("enter an animal ")
# anim3 = input("enter an animal ")
# if anim1 == "monkey" or anim2 == "monkey" or anim3 == "monkey":
#     print("Go bananas")
# else:
#     print("this is a boring zoo ")
#################
#counting
# count = 0
# while count < 10:
#     print(count)
#     count = count + 1
# #####################################################3
# #keep asking the user for pineapple
# while True:
#     topping = input("what do you want your toppings to be? ")
#     if topping == "exit":
#         print("ok sending your order......")
#         break
#     else:
#         print("ok added",topping)
#2 Question riddle
# import random
# num1 = random.randint(30,70)
# num2 = random.randint(30,70)
# while True:
#     uinput = int(input("what is {} + {}? ".format(num1,num2)))
#     if uinput == num1 + num2:
#         print("correct!")
#         break
#     else:
#         print("wrong")
# while True:
#     input = int(input("what is 10 + 30? "))
#     if input == 40:
#         print("correct")
#         break
#################################################
#check that the code is 4 characters long
# while True:
#     otp = input("what is the OTP? ")
#     if len(otp) != 4:
#         print("OTP must be 4 digits try again")
#     else:
#         print("OTP accepted")
#         break

#Do this challenge
'''
Question 3 (Range Check):
Write the input entry and validation code for a program 
that needs to accept a secondary student's age.

The age must be between 13 and 16 inclusive.

If the input is invalid, your code should keep trying 
by asking for the input to be entered again.

Sample output:
Enter age: 12
Invalid input. Age must be between 13 and 16.
Enter age: 20
Invalid input. Age must be between 13 and 16.
Enter age: 16
Age accepted.
'''
#Username checker only lowercase allowed
# while True:
#     inpute = input("Enter a username all lowercase ")
#     if inpute.islower():
#         print("Accepted")
#         break
#     else:
#         print("Username denied try again")
