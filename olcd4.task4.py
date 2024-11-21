'''
2018 - Task 4 [20]
You have been asked to create a guessing game program.
The program should:
- Allow player 1 to input a whole number between 
1 and 50 inclusive, for player 2 to guess. 

There must be validation present to check that the 
number entered is between 1 and 50 inclusive.

-	Allow player 2 to have 5 guesses to correctly guess 
the number input by player 1. 
You do not need to validate the input for player 2.

-	Output “You guessed the correct number.” 
When player 2 inputs the same number as player 1. 
The game must end if the correct number is guessed.

-	Output “You did not guess the correct number.” 
When player 2 does not input the same number as player 1.

-	Output “Game over!” when player 2 has five incorrect guesses.
'''

'''
10.	Write your program and test that it works.
[10]
'''
# Write and test your code here
#This is a program for a game
inpute = int(input("Player 1 input a number 1-50 "))
while True:
    if inpute >= 1 and inpute <= 50:
        print("thank you player 1")
        break
for count in range(5):
    inpute2 = int(input("Player 2 enter a number 1-50 "))
    if inpute2 == inpute:
        print("You guessed the correct answer")
        break
    else:
        print("You did not guess the correct answer")
else:
    print("You used up all your chances")







##### END QUESTION
'''
11.	When your program is complete, test it for the following:
a.	Test 1 - Player 1 inputs the number 55
b.	Test 2 - Player 1 inputs the number 0
c.	Test 3 - Player 1 inputs the number 10 and player 2 guesses 
    the numbers 15 and 10
d.	Test 4 - Player 1 inputs the number 20 and player 2 guesses 
    the numbers 30, 35, 22, 15, 49
[4]
'''
# Test Your Code ABOVE



##### END QUESTION
'''
12.	
Extend your program to identify if player 2's 
guess is lower or higher than the number input by player 1. 
A suitable message must then be output.

Save your program.
[2]
'''
# Copy your code from above. Write and test your code here




##### END QUESTION
'''
13.	

Extend your program to allow player 2 to choose an 
easy, medium or hard game. 

An easy game allows eight guesses, a medium game allows 
six guesses and a hard game allows four guesses.

If player 2 inputs a correct guess, the program must output the 
number of guesses made.

You are not required to validate the input for player 2.

Save your program.
[4]
'''
#Improved game program
# Copy your code from above. Write and test your code here
# inpute = int(input("Player 1 input a number 1-50 "))
# while True:
#     if inpute >= 1 and inpute <= 50:
#         print("thank you player 1")
#         break
# modeselect = input("Select easy,medium or hard ")
# if modeselect == "easy":
#     for c in range(8):
#         if inpute2 == inpute:
#             print("You guessed the correct answer")
#             print("You made",8 - c, "guesses")
#             break
#         else:
#             print("you guessed the wrong answer")
# if modeselect == "medium":
#     for b in range(6):
#         if inpute2 == inpute:
#             print("Congrats you got the correct answer")
#             print("You made",6-b,"guesses")
#             break
#         else:
#             print("You guessed the wrong answer")
# if modeselect == "hard":
#     for a in range(4):
#         if inpute2 == inpute:
#             print("Congrats you got the correct answer")
#             print("You made",4 - a ,"guesses")
#             break
#         else:
#             print("You guessed the wromg answer")
        
