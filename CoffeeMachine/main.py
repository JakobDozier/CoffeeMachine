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

def check_resources(drink):
    for ingredient in drink:
        if resources[ingredient] < drink[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def check_coins(cost):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_quarters_amount = round(quarters * 0.25, 2)
    total_dimes_amount = round(dimes * 0.10, 2)
    total_nickels_amount = round(nickels * 0.05, 2)
    total_pennies_amount = round(pennies * 0.01, 2)

    total_amount = round(total_quarters_amount + total_dimes_amount + total_nickels_amount + total_pennies_amount, 2)

    if total_amount == cost:
        print("Thank you for exact change!")
        return True
    elif total_amount > cost:
        change = round(total_amount - cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def update_resources(used_resources):
    for ingredient in used_resources:
        resources[ingredient] -= used_resources[ingredient]

def start_coffee_machine():
    money = 0
    machine_running = True

    while machine_running:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")

        if user_choice == "report":
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money: ${money}")
        elif user_choice == "off":
            machine_running = False
        else:
            user_choice_ingredients = MENU[user_choice]["ingredients"]
            user_choice_cost = MENU[user_choice]["cost"]
            if check_resources(user_choice_ingredients):
                if check_coins(user_choice_cost):
                    money += user_choice_cost
                    update_resources(user_choice_ingredients)
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"Keep going money now at: {money}")
                else:
                    print("Time to stop 2")
            else:
                print("Time to stop")

start_coffee_machine()