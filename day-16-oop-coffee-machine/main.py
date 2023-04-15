from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create coffee objects
latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)

# Create Menu, CoffeeMaker objects
menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

# Set is_on flat
is_on = True

while is_on:

    # Get menu options
    options = menu.get_items()

    # Prompt user by asking "What would you like? (espresso/latte/cappuccino):
    choice = input(f"What would you like? ({options}): ")

    # Turn off coffee machine by entering "off" to the prompt.
    if choice == "off":
        is_on = False
    # Print report if "report" is chosen
    elif choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        # Find drink based on user's input
        drink = menu.find_drink(choice)
        # Check if there is sufficient ingredients to make
        can_make = coffeemaker.is_resource_sufficient(drink)
        # If can_make = True, ask users to pay money
        if can_make is True:
            cost = drink.cost
            print(f"A {choice} costs ${cost}.")
            # Process payment
            payment_successful = money_machine.make_payment(cost)
            # Make coffee if payment is successful
            if payment_successful is True:
                coffeemaker.make_coffee(drink)
