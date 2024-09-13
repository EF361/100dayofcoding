#this is a guessing game

import random

number = random.randint(1,20 )
guess = int(input("Enter a number between 1 - 20 : "))

if guess < 0 or guess > 20: 
    print(f"The number you enter is out of range. ")
else: 
    if guess == number: 
        print(f"You guessed it right! The number was {guess}")
    elif guess < number: 
        print(f"Your number is smaller! Try again")
    elif guess > number: 
        print(f"Your number is bigger! Try again")

