MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def check_resources(user_input):
    c = 0
    order_ingredients = MENU[user_input]['ingredients']
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            c += 1
            print(f'Sorry there is not enough {item}.')
    if c > 0:
        return False
    else:
        return True


def take_money(user_input):
    global money
    cost = MENU[user_input]['cost']
    order_ingredients = MENU[user_input]['ingredients']
    print(f"Cost of {user_input}: ${cost}")
    print('Please insert coins:')
    quarters = int(input('How many quarters ($0.25)? '))
    dimes = int(input('How many dimes ($0.10)? '))
    nickles = int(input('How many nickles ($0.05)? '))
    pennies = int(input('How many pennies ($0.01)? '))
    amount_paid = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    print(f"Amount paid by customer: {amount_paid:.2f}")
    if amount_paid > cost:
        amount_refunded = amount_paid - cost
        money += cost
        print(f'Here is {amount_refunded:.2f} in change.')
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is your {user_input} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


machine_on = True
while machine_on:
    user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        if check_resources(user_input):
            take_money(user_input)
    elif user_input == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}ml\n"
              f"Money: ${money}")
    elif user_input == 'off':
        machine_on = False
    else:
        print("Please enter correct choice") 
