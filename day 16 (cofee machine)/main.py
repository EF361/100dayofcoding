from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

game_on = True
menu = Menu()
money_machine = MoneyMachine()
coffeeMaker = CoffeeMaker()

while game_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        game_on = False

    elif choice == "report":
        coffeeMaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and money_machine.make_payment():
            coffeeMaker.make_coffee(drink.cost)
