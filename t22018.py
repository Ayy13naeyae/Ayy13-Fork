'''
The following program allows the weights of 15 bags of rice to be input. 
The correct weight for each bag of rice must be 
between 4.9 kg and 5.1 kg inclusive.
'''
# bags_rice = 15
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")
'''
Open the file RICEBAGS.py
Save the file as MYBAGS_<your name>_<center number>_<index number>.py

1.	Edit the program so that it:
a.	Accepts the weights for only 10 bags of rice.
[1]
'''

'''
b.	Prints out the message “The bag of rice is the correct weight” 
when a weight entered is between 4.9kg and 5.1 kg inclusive.
[2]
'''
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the kg of the bag of rice "))
#     if bag_weight <= upper_bound and bag_weight >= lower_bound:
#         print("The bag of rice is the correct weight")
#     else:
#         print("The bag of rice is either underweight or overweight")

'''
c.	Prints out the number of bags of rice that were underweight, 
as well as the number that were overweight, after the weights of 
all the bags have been entered.
[5]
'''

'''
Save your program.
2.	Save your program as VARBAGS_<your name>_<center number>_<index number>.py
Edit your program so that it works for any number of bags of rice.
Save your program.
[2]
'''

'''
2020 - Task 2 [10]
The following program checks it the personal identification number (PIN) 
entered for a locker is correct. There are 10 lockers available and the 
correct PIN for each locker is stored in an array.
A PIN cannot start with the digit 0.

The program allows the user to enter the number of the locker they 
want to open, and a PIN. It checks if the PIN is correct for that locker.
'''
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = float(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")

'''
1.	Edit the program so that it converts the PIN input 
by the user to an integer.
Save your program
[1] 
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# locker = int(input("Please enter the locker you would like to open: "))
# pin = int(input("PLease enter the PIN for the locker: "))
# if pin == arraypins[locker-1]:
#     print("The locker is open.")
# else: 
#     print("Incorrect PIN for that locker")


'''
2.	Edit the program to only accept a locker number between 1 and 10 
(inclusive) to be input. A suitable error message must be displayed 
if the locker number input is not in this range. The program must 
loop until a valid locker number is input.
Save your program.
[3]
'''
# Write and test your code here
# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# while True:
#     locker = int(input("Please enter the locker you would like to open: "))
#     if locker >=1 and locker <=10:
#         print("Valid locker")
#         break
#     else:
#         print("Invalid locker")

# pin = int(input("PLease enter the PIN for the locker: "))

'''
3.	Edit the program to only accept a PIN of 4 digits to be 
entered by the user. A suitable error message must be displayed 
if an incorrect input is given. The program must loop until the PIN 
input is 4 digits.
Save your program
[3]
'''
# Write and test your code here
arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
while True:
    locker = int(input("Please enter the locker you would like to open: "))
    if locker >=1 and locker <=10:
        print("Valid locker")
        break
    else:
        print("Invalid locker")
pin = int(input("PLease enter the PIN for the locker:"))
if pin <=3:
    print("invalid password")
    
    


'''
4.	Edit the program to loop until the user inputs both a 
correct locker number and the matching PIN for that locker.
Save your program.
[3]
'''

# arraypins = [1234, 1654, 1936, 3957, 2058, 7689, 2749, 2265, 1010, 9966]
# while True:
#     locker = int(input("Please enter the locker you would like to open: "))


#     if locker == 0:
#         pin1 = input("Enter locker 0 PIN ")
#         if pin1 == 1234:
#             print("Locker 0 Open")
#             break
#         else:
#             print("Invalid PIN")
#     if locker == 1:
#         pin1 = input("Enter locker 1 PIN ")
#         if pin0 == 1654:
#             print("Locker 1 Open")
#             break
#         else:
#             print("Invalid PIN")









# Write and test your code here
