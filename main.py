from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()
coffee_maker.report()

def coffee_machine():
    """
    A simple coffee machine simulator.

    This script allows users to interact with a coffee machine:
    - Turn it on/off.
    - Check resource and money status.
    - Select and purchase drinks from a menu.

    Usage:
    1. Start the script to begin using the coffee machine.
    2. Follow the prompts to choose drinks or request reports.
    3. Enter 'off' to turn off the machine.
    4. Enter 'report' to get current machine status.
    5. Select a drink to check availability and make a purchase.

    Modules Used:
    - Menu: Provides a list of available drinks.
    - CoffeeMaker: Checks and manages resources for drink preparation.
    - MoneyMachine: Handles payments and maintains money status.

    Ensure all modules ('menu', 'coffee_maker', 'money_machine') are properly implemented and imported.
    """
    is_on = True

    while is_on:
        options = menu.get_items()
        user_choice = input(f"What would you like? ({options}): ").lower()
        if user_choice == "off":
            is_on = False
        elif user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_choice)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                else:
                    print("Insufficient resources or payment failed. Please try again.")
            else:
                print("Invalid choice. Please select from available options.")

if __name__ == "__main__":
    coffee_machine()
