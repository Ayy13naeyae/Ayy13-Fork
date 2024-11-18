# print("hello world")
# #printing
# print("hello")
# print("my name is Axl")
# print("my hobby is games")
# x = 10
# y = 20
# z = x + y
# print(z)
# #variables
# hobby = "game"
# print ("i like to",hobby)
# name = "axl"
# title ="king"

# print("You shall know me as", name, title )
# #math
# num1 = 200
# num2 = 300
# print(num1 + num2)

#input
# name = input("what is thy name, sire?" )
# command = input("what is thy command?" )

# print(name, "commands the peasants to", command)
#simple addition programming
# num1 = int(input("what is the first number? "))
# num2 = int(input("what is the second number? "))
# answer = num1 + num2
# print(answer)

###############
#for loops
#for i in range(10):
#    print("hello") #indentation
# for k in range(3):

#     for i in range(3):
#         print("hello")
#     for i in range(3):
#         print("bye")
###################
#cheer program
#name = input("who to cheer" ) #axl #incomplete
# for i in name:
#     ("print give me",i)

#counting numbers
# for i in range(67,97):
#     print(i)
# for i in range(6,78,6): #multiplication
#     print(i)
#for i in range(15,0 , -1): #counting down from 15 to 1
#     print(i)
#caculate allowance for 4 years
# name = input("what is your name? ")
# allowance = int(input("what is your weekly allowance? "))
# for i in range(4):
#     print(allowance*52)
################
#caculate length of person full name
#first name and last name
# fname = input("enter first name ")
# lname = input("enter last name ")
# total = len(fname) + len(lname)
# print("the total length of", fname , lname ,"is", total)
############
#random number generation
# import random
# for i in range(7):
#     num = random.randint(1,47)
#     print(num)
###########
#empty list
import random
rannums = [] #have a list of numbers
while len(rannums) < 6:
    num = random.radint(1,47)
    if num not in rannums:
        rannums.append(num)
print(rannums)


