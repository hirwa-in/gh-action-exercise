from menu import Menu
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino/): ")
    items = ["espresso", "latte", "cappuccino"]
    if user_choice == "off":
        break
    elif user_choice == "report":
        coffe_maker.report()

    elif user_choice in items:
        drink = menu.find_drink(user_choice)

        if drink:
            sufficient = coffe_maker.is_resource_sufficient(drink)
            cost = drink.cost
            if sufficient:
                money_machine.make_payment(cost)
                if sufficient:
                    coffe_maker.make_coffee(drink)

