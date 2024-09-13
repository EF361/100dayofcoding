import random
from logo import logo
from clear import clear


def total_score(total, score):
    """Calculate and display the total score after the questions."""

    final_score = (score / total) * 100
    print(f"\nFinal Score: {final_score:.2f}%")
    if final_score >= 90:
        print("You're brilliant!")
    elif final_score >= 80:
        print("Not bad. Keep up!")
    elif final_score >= 50:
        print("Try harder.")
    elif final_score >= 40:
        print("Almost fail.")
    else:
        print(".....")


def ask_question(question_num, num1, num2, operator):
    """Ask a math question and return whether the answer was correct."""

    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    elif operator == "x":
        correct_answer = num1 * num2

    user_answer = input(f"{question_num}: {num1} {operator} {num2} = ")
    try:
        user_answer = int(user_answer)
        if user_answer == correct_answer:
            print("Correct Answer!\n")
            return True
        else:
            print("Wrong answer!\n")
            return False
    except ValueError:
        print("Invalid input. Answer should be a number.")
        return False


def math_quiz():
    """Main function to run the math quiz."""

    cont = True
    symbols = ["+", "-", "x"]

    while cont:
        print(logo)
        print("Welcome to the Math Quiz.")
        try:
            times = int(input("How many questions do you want to do? \n"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        total = 0
        score = 0

        for i in range(times):
            num1 = random.randint(0, 30)
            num2 = random.randint(0, 30)
            operator = random.choice(symbols)
            total += 1

            if ask_question(total, num1, num2, operator):
                score += 1

        total_score(total, score)

        to_continue = input("Next set of questions? 'y' or 'n': ").lower()
        if to_continue == "y":
            clear()
        elif to_continue == "n":
            cont = False
            clear()
        else:
            print("Invalid input. Exiting quiz.")
            cont = False
            clear()


if __name__ == "__main__":
    math_quiz()
