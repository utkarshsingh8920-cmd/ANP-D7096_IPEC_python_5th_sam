"""
A secret number is 37. 
Keep asking the user to guess the number until the correct number is entered. 
Display whether the entered number is too high, too low, or correct.
"""
#----------------------------Coding section----------------------------------------------
secret = 37
guess = 0
#--------------------------------------------------------
while guess != secret:
        guess = int(input("Guess the Number: "))
        if guess < secret:
            print("Too Low")
        elif guess > secret:
            print("Too High")
        else:
            print("Correct!")
#--------------------------------------------------------------
"""Output :
Guess the Number: 34
Too Low
Guess the Number: 343
Too High
Guess the Number: 54
Too High
Guess the Number: 37
Correct!
"""
