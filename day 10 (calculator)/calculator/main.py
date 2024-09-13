import art
import clear


# define functions
# add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return n1 / n2


# dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

exit = False

# main program
while not exit:
    print(art.logo)
    # make condition for the calculator
    continue_calculation = True

    # first number
    num1 = float(input("What is the first number? : "))

    while continue_calculation:
        # ask user for operation
        for symbol in operations:
            print(symbol)

        symbol = input("Pick an operation: ")

        # second number
        num2 = float(input("What is the second number? : "))

        # determine suitable functions for the operation choose
        function = operations[symbol]
        answer = function(num1, num2)

        # print the answer
        print(f"{num1} {symbol} {num2} = {answer} ")

        # continue the operation or cancel
        cont = input(
            f"for exit: exit\nfor continue calculation with {answer}: 'y'\nfor new calculation: 'n'\n"
        ).lower()
        num1 = answer
        if cont == "n":
            continue_calculation = False
            clear.clear()
        if cont == "exit":
            continue_calculation = False
            exit = True
            print("Thanks for using our calculator.")
