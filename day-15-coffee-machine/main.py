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
    "money": 0.0
}


# Defining helper functions
def print_report(resources_dict):
    """Takes resources as input, and prints a report of the available resources"""
    print("\n")
    print(f"Water: {resources_dict['water']}ml")
    print(f"Milk: {resources_dict['milk']}ml")
    print(f"Coffee: {resources_dict['coffee']}g")
    print(f"Money: ${resources_dict['money']}")
    print("\n")


def check_resources(coffee_order):
    """Checks if the coffee machine has enough resources to make the specified coffee order.
    Returns a boolean value; True if the machine has enough resources, False otherwise.
    If there are insufficient resources, a message will be printed for each resource."""
    enough_resources = True
    for ingredient in MENU[coffee_order]["ingredients"]:
        if resources[ingredient] < MENU[coffee_order]['ingredients'][ingredient]:
            print(f"There is not enough {ingredient}.")
            enough_resources = False
    return enough_resources


def process_money(coffee_order):
    """
    Given a coffee order (espresso, latte, or cappuccino), prompts the user to insert coins (quarters, dimes,
    nickles, and pennies) and calculates the total money paid. The function then checks if the paid amount is
    enough to cover the cost of the coffee order.

    Args:
        coffee_order (str): The type of coffee order (espresso, latte, or cappuccino).

    Returns:
        bool: True if the paid amount is equal to or greater than the cost of the coffee order, otherwise False.
    """
    # Get the price of the coffee order
    coffee_price = MENU[coffee_order]['cost']
    # Print the coffee order price
    print(f"A {coffee_order} costs ${coffee_price}.")
    # Prompt the user to insert coins
    print("Please insert coins.")
    # Get the money from the user
    n_quarters = int(input("How many quarters?: "))
    n_dimes = int(input("How many dimes?: "))
    n_nickles = int(input("How many nickles?: "))
    n_pennies = int(input("How many pennies?: "))

    # Calculate the total money paid in cents
    money_paid = ((n_quarters * 25) + (n_dimes * 10) + (n_nickles * 5) + (n_pennies * 1)) / 100
    # Check if the paid amount is sufficient for the coffee order
    paid_enough = money_paid >= coffee_price
    # Calculate change if paid_enough == True
    change = 0
    if paid_enough is True:
        change = money_paid - coffee_price
    return paid_enough, change


# Main program
def coffee_machine():

    # Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off coffee machine by entering "off" to the prompt.
    if user_input == "off":
        return

    # Print report when user enters "report" to the prompt.
    if user_input == "report":
        print_report(resources)
        coffee_machine()

    # When user chooses drink, the program should check if there are enough resources to make that drink.
    if user_input in ["espresso", "latte", "cappuccino"]:

        # Check whether there are enough resources to make that drink
        enough_resources = check_resources(user_input)

        # If enough resources, print price of coffee, and prompt user to insert coins
        if enough_resources is True:
            paid_enough, change = process_money(user_input)

            # Make coffee if paid enough, and issue change to user
            if paid_enough is True:
                print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕️. Enjoy!")
                # Update resources
                for ingredient in MENU[user_input]["ingredients"]:
                    resources[ingredient] -= MENU[user_input]['ingredients'][ingredient]
                # Update money in machinela
                resources["money"] += MENU[user_input]['cost']
                # Restart program
                coffee_machine()

        # Else, refund money, and restart program
        else:
            print("Sorry, that's not enough money. Money refunded.")
            coffee_machine()


# Initiate program
coffee_machine()
