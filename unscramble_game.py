# WORD UNSCRAMBLE CODE
import random
words = [
    "python", "computer", "education", "coding", "programming", 
    "algorithm", "debugging", "variable", "function", "software",
    "hardware", "keyboard", "internet", "database", "network", 
    "browser", "website", "developer", "compiler", "iteration", 
    "condition", "looping", "syntax", "recursion", "automation", 
    "simulation", "encryption", "framework", "datascience", "interface"
]
# choose a word randomly
word = random.choice(words)
print(word)

#split this into characters in a list
charlist = list(word)
print(charlist)

# shuffle the items in a list
random.shuffle(charlist)
print(charlist) #After shuffle

# put the list back into a string
scrambled = ''
for c in charlist:
    scrambled = scrambled + c + ''

# while true
while True:
    #display the word
    print("Can you guess the word? ")
    print(scrambled)
    


    # options Type 1 to scramble again, 2 to guess, 3 to give up:
    uoption = input("Type 1 to scramble again,Type 2 to answer, Type 3 to give up,Type 4 to cheat ")

    # if option 1
    if uoption == "1":
        random.shuffle(charlist)
        scrambled = ''
        for c in charlist:
            scrambled = scrambled + c + ''

    # elif option 2
    if uoption == "2":
        uguess = input("so, what is the word? ")
        if uguess == word:
            print("Correct: {} was the word!".format(word))
            break
        else:
            print("Wrong,try again")
    
    # elif option 3
    if uoption == "3":
        print("The answer was {}".format(word))
        break
    if uoption == "4":
        print("why you cheating")
        print("The answer was {}".format(word))
    # else invalid
    else:
        print("Only option 1,2 or 3 ")