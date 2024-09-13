from art import logo
import random
import clear


def guessGame(times, number):
    """guessing system"""

    # for loop to loop through the attempts
    for i in range(times):
        print(f"You have {times - i} attempts.")
        guess = int(input("\nGuess a number : "))
        while guess < 0 or guess > 100:
            print("Number is out of range. ")
            guess = int(input("\nGuess a number : "))
        if guess == number:
            # correct answer return true and break
            print("Bingo! You win! ")
            return True
        elif guess > number:
            print("Too high!")

        elif guess < number:
            print("Too low.")
    # trigger only if attempt finish and user cannot guess the output
    return False


def welcome():
    """before the guessing game start"""
    print(logo)
    number = random.randint(0, 100)
    print("Welcome to Guessing Game. You need to choose a number between 0-100.\n")

    # set mode
    mode = input("Easy or Hard? : ").lower()
    while mode not in ["easy", "hard"]:
        print("Invalid input.")
        mode = input("Easy or Hard? : ").lower()

    if mode == "easy":
        times = 10
    elif mode == "hard":
        times = 5

    result = guessGame(times, number)
    if not result:
        print("You lose. Attempt finished. ")

    to_continue = input("Continue? (Y/N): ")

    while to_continue not in ["y", "n"]:
        to_continue = input("Continue? (Y/N): ")
    if to_continue == "y":
        clear.clear()
        return True

    elif to_continue == "n":
        clear.clear()
        return False


while welcome():
    pass
