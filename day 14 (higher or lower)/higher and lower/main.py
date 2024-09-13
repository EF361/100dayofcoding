import random
from art import logo, vs
from game_data import data
from clear import clear


def format_data(account):
    """format data into printable format, return string"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}."


def check_answer(user_guess, a_followers, b_followers):
    """check answer and return bool statement"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# print logo, score, game_should_continue
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:  # if condiition is true, continue the loop
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Againts B: {format_data(account_b)}")

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    guess = input("Who has more followers? : ").lower()

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(clear())
        print(logo)
        print(f"You are right! Current score {score}")

    else:
        print(f"You are wrong! Final score {score}")
        game_should_continue = False
