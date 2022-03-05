from replit import clear
from time import sleep
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


def show_resources(resources):
    print("*" * 33)
    for item in resources:
        print("*", f'{item:^12}', '*', f"{resources[item]:^ 14}", "*")
    print("*" * 33)


def check_resources(choice, resource):
    valid = True
    print(choice)
    print(resource)
    for item in choice['ingredients']:
        if choice['ingredients'][item] > resource[item]:
            print('choice´e maior', item)
            valid = False
    return valid


def get_choice():
    valid = False
    while not valid:
        ans = input()
        if not (ans in ['espresso', 'latte', 'cappuccino']):
            print("Invalid answer")
        else:
            valid = True
    return ans


def int_validate():
    valid = False
    while not valid:
        try:
            choice = int(input())
        except ValueError:
            print("Please enter with a integer value.")
        else:
            valid = True

        return choice


def get_payment(money):
    coins = {
        "penny": 0.01,
        "nickel": 0.5,
        "dime": 0.1,
        "quarter": 0.25
        }

    for coin in coins:
        print(f"How many {coin}?")
        money += int_validate() * coins[coin]

    return money


def quest_confirm():
    ans = -1
    while not (ans in [0, 1]):
        ans = int_validate()

    return ans == 1


def action(choice, money, resources):
    for item in choice['ingredients']:
        resources[item] -= choice['ingredients'][item]

    money -= choice['cost']

    return money, resources


def main():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    coffee = True
    money = 0
    while coffee:
        clear()
        show_resources(resources)
        print(f"Money: {money}")

        print('Would you like? (espresso/latte/cappuccino):', end='')
        choice = MENU[get_choice()]

        if not check_resources(choice, resources):
            print('We have no resources to make this recipe... Sorry!')
        else:

            # check money
            while money < choice["cost"]:
                print('You have no sufficient founds. Do you wanna to insert some money? [0] no || [1] yes', end='')

                if quest_confirm():
                    money = get_payment(money)

            money, resources = action(choice, money, resources)

        sleep(0.7)


main()
