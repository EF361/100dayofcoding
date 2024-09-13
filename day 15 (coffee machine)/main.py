# functionalities
# 1. TODO: print report ✅
# 2. TODO: check resources sufficient✅
# 3. TODO: process coins✅
# 4. TODO: check transaction successful ✅

# import modules
from art import logo, icon
from data import resources, MENU
from clear import clear

earnings = 0.00


def report(resources, earnings):
    """generate remain resources, return string"""
    resource_water = resources["water"]
    resource_milk = resources["milk"]
    resource_coffee = resources["coffee"]
    return f"Water: {resource_water}ml\nMilk: {resource_milk}ml\nCoffee: {resource_coffee}ml\nMoney: ${earnings}"


def check_resource(order_ingredients):
    """check whether resources is enough, return bool"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def payment():
    """process payment, return double"""
    total = 0.00
    print("\nPress make payment: ")
    total += int(input("Insert quarters ($0.25): ")) * 0.25
    total += int(input("Insert dimes ($0.10): ")) * 0.10
    total += int(input("Insert nickles ($0.05): ")) * 0.05
    total += int(input("Insert pennies ($0.01): ")) * 0.01
    print(f"Your total payment: {round(total,2)}")
    return total


def is_transaction_successful(money, cost):
    """check whether money insert is enough, return bool"""
    if money >= cost:
        global earnings
        earnings += cost
        if money > cost:
            change = round(money - cost, 2)
            print(f"Here is your ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def make_coffee(coffee_name, item_ingredients):
    """make coffee and print output"""
    for items in item_ingredients:
        resources[items] -= item_ingredients[items]
    print(f"Here is your {coffee_name}. {icon}")


print(logo)

to_continue = True

while to_continue:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino) : ")

    if choice == "off":
        clear()
        to_continue = False
    elif choice == "report":
        print(report(resources, earnings))
    else:
        drinks = MENU[choice]
        print(f"Total Price for {choice} : ${round(drinks["cost"],2)}")
        if check_resource(drinks["ingredients"]):
            money = payment()
            if is_transaction_successful(money, drinks["cost"]):
                make_coffee(choice, drinks["ingredients"])
