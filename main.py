# Imports random module to be used in program!
import random

# range_start and range_end variables declared to determine range for game. Is important to note range_start is inclusive, range_end exclusive, meaning start includes given value, end excludes given value.
range_start = 1
range_end = 10
# rng_choice variable takes the random modules .randint() function, and passes a start and end point to randomly generate a number that falls inbetween these two given points.
rng_choice = random.randint(range_start, range_end)
# user_choice variable records users guess.
user_choice = input(f"Guess a number between 0 and {range_end}, only enter your number in its integer form(1,2,3,4,5,6,7,8,9).\n")

# Checks to see if users choice is in fact a number, if not, prints out an error message to explain to the user what occured.
if user_choice.isdigit():
    
    # Checks users given number to see if it falls within the valid range, if not, error message is given, if valid, goes to final step to see if users choice matches rng_choice.
    if int(user_choice) == int(rng_choice):
        print("YOU WIN!") # YOU WON -- GAME OVER!
    elif int(user_choice) not in range(range_start,range_end):
        print(f"Choice not within given range of 0-{range_end}. Try again!") # NUMBER NOT VALID -- TRY AGAIN!
    else:
        print("YOU LOSE!") # YOU LOST -- GAME OVER!
        
else:
    print("Valid answer not given. Only numbers between 0-{range_end} entered as an integer(1,2,3,4,5,6,7,8,9), not spelled out('One','Two','Three', etc), will be accepted.") # ERROR -- INTEGER NOT GIVEN!