import random
import clear
from art import logo

# set the limit for the game
limit = 21


def deals_cards(user, times):
    """deal cards based on the time mention"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    for number in range(times):
        number = random.choice(cards)
        user.append(number)


def calculate(user):
    """calculate the total number based on the cards given"""

    return sum(user)


def blackjack(total_user, total_computer):
    """check whether computer or user got a blackjack. return bool statement"""

    if total_computer == limit:
        print("Computer got a BLACKJACK!")
        print("You lose. ")
        return True
    elif total_user == limit:
        print("You got a BLACKJACK!")
        print("You win! ")
        return True


def compare(total_user, total_computer):
    """compare whether who lose or win"""

    if total_user > limit and total_computer > limit or total_computer == total_user:
        print("It's a draw. ")
    elif total_user > limit:
        print("You lose.")
    elif total_computer > limit:
        print("You win!")
    elif total_user > total_computer:
        print("You win! Congrats. ")
    elif total_computer > total_user:
        print("You lose. ")


# declare the condition for the whole game
game = True

while game:
    print(logo)
    # declare variables
    user_cards = []
    computer_cards = []

    total_user = 0
    total_computer = 0

    isBlackjack = False
    cont = True

    # first deal card and calculate the total
    deals_cards(user_cards, 2)
    deals_cards(computer_cards, 2)
    total_user = calculate(user_cards)
    total_computer = calculate(computer_cards)

    # display output
    print(f"Your Cards: {user_cards}\nCurrent Score: {total_user}\n")
    print(f"Computer's First Card: {computer_cards[0]}")

    # check whether computer or user has blackjack
    isBlackjack = blackjack(total_user, total_computer)

    if not isBlackjack:
        # user plays
        while cont:
            condition = input("Type 'Y' to Continue or 'N' to pass : ").lower()
            if condition == "y":
                deals_cards(user_cards, 1)
                total_user = calculate(user_cards)
                print(f"\nYour Cards: {user_cards}\nCurrent Score: {total_user}\n")
                print(f"Computer's First Card: {computer_cards[0]}")

                if total_user > limit:
                    for number in range(len(user_cards)):
                        if user_cards[number] == 11:
                            user_cards[number] = 1
                            total_user = calculate(user_cards)
                            print("\nYour ace has changed from 11 to 1.")
                            print(
                                f"Your Cards: {user_cards}\nCurrent Score: {total_user}\n"
                            )
                            print(f"Computer's First Card: {computer_cards[0]}")

                    if total_user > limit:
                        cont = False

            elif condition == "n":
                cont = False

        # computer plays
        while total_computer < 16:
            deals_cards(computer_cards, 1)
            total_computer = calculate(computer_cards)

        # Final Output
        print("\n\nFinal Output: ")
        print(f"Your Cards: {user_cards}\nCurrent Score: {total_user}\n")
        print(f"Computer Cards: {computer_cards}\nComputer's Score: {total_computer}\n")
        compare(total_user, total_computer)

    condition = input("Would you like to restart the game? 'y' or 'n': ").lower()
    if condition == "n":
        game = False
    clear.clear()
