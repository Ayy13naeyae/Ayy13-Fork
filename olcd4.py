'''
2018 - Task 3 [10]
The following program should identify if a student receives either 
a gold, silver or bronze award for joint achievement in Computing 
and Mathematics. 
Each student has taken a test in Computing and a test in Mathematics. 

The program uses the rules:
- A student receives a gold award for a test score of 
100 or greater in both Computing and Mathematics.

- A student receives a silver award for a test score 
of 100 or greater in Computing or Mathematics. 

They also need a combined Computing and Mathematics
score of 180 or greater.

- A student receives a bronze award for a test score 
of 75 or greater in both Computing and Mathematics.

The test scores are whole numbers only. 
The program finishes when there are no more 
student test scores to be input. 

The award a student receives is output after the 
test scores for that student are input.

There are several syntax and logic errors in the program.

9. Identify and correct the errors in the program so 
that it works according to the rules given. 
Save your program.
[10]

'''

# students = False
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score"))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if more_scores == 'N':
#         students = True
#     else:
#         students = True
students = True #THIS IS A BACKUP #CHANGED THIS INTO TRUE
while students == True:
    comp = int(input("Enter the Computing test score "))
    math = int(input("Enter the Mathematics test score" )) # MISSING # MARK
    joint_score = comp + math #FIXED COMP + COMP
    if comp >= 100 and math >= 100:
        print("Student is awarded a gold award")
    elif (comp >= 100 and math >= 100) and joint_score >= 180: #FIXED WRONG
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
    if more_scores == 'N' or "No" or "n" or "NO": #MADE "MORE" FROM MORE SCORES LOWERCASE
        students = False #CHANGE TO FALSE TO BREAK OUT OF THE LOOP
    else: #MISPELLED ELSE
        students = True

#     students = False #ORIGINAL QUESTION UNEDITED
# while students == True:
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     ekse:
#         students = True