from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    user_input = input('What would you like? ' + menu.get_items() + ': ').lower()
    if user_input == 'report':
        coffee_machine.report()
        money_machine.report()
    elif user_input == 'off':
        machine_on = False
    else:
        user_drink = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(user_drink) and money_machine.make_payment(user_drink.cost):
            coffee_machine.make_coffee(user_drink)
