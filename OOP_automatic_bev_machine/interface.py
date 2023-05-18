"""
User interface
for fully automatic beverage machine program
"""

from beverage import Beverage, Condiments


class UserInterface:

    # Print menu to the user: --------------------------------------------
    def show_menu():
        print('Welcome to your fully automatic beverage vending machine!')
        print()
        print('BEVERAGE MENU -------------------------------------------')
        print('Coffees:')
        print('  [1] Espresso')
        print('  [2] Americano')
        print('  [3] Latte')
        print('Teas:')
        print('  [4] Black tea')
        print('  [5] Green tea')
        print('  [6] Yellow tea')
        print('---------------------------------------------------------')

    # Ask user for their beverage selection: ----------------------------
    def user_selection():
        print('Input the number corresponding to your beverage selection: ')
        try:
            beverage_request = int(input())
        except ValueError:
            print('Please enter a number only.')
            beverage_request = int(input())

        while beverage_request < 1 or beverage_request > 6:
            print('Please enter a valid number corresponding to your beverage selection:')
            try:
                beverage_request = int(input())
            except ValueError:
                print('Please enter a number only.')
                beverage_request = int(input())

        # Create beverage order based on user input ------------------------
        if beverage_request == 1:
            beverage = Beverage(name='Espresso', price=3.00, caffeine=300, calories=10)
            print(beverage)
        elif beverage_request == 2:
            beverage = Beverage(name='Americano', price=3.50, caffeine=350, calories=20)
            print(beverage)
        elif beverage_request == 3:
            beverage = Latte(name='Latte', price=4.50, caffeine=300, calories=250)
            print(beverage)
        elif beverage_request == 4:
            beverage = Tea(color='Black', name='tea', price=3.00, caffeine=100, calories=5)
            print(beverage)
        elif beverage_request == 5:
            beverage = Tea(color='Green', name='tea', price=3.00, caffeine=100, calories=5)
            print(beverage)
        elif beverage_request == 6:
            beverage = Tea(color='Yellow', name='tea', price=3.00, caffeine=100, calories=5)
            print(beverage)

        # Simulate brew ---------------------------------------------------
        print(f'Now brewing your {beverage.name} .....')
        print()
        print('Brewing finished!')
        print()

    def ask_condiments():
        # Ask user for condiments -----------------------------------------:
        print('CONDIMENT OPTIONS ------------------------------------------')
        print('  - Milk')
        print('  - Sugar')
        print('  - (Only 3 units of condiments total allowed)')
        print()
        # Ask for milk:
        print('Would you like to add milk to your beverage?')
        print('  [0] No')
        print('  [1] Yes')
        try:
            milk_request = int(input())
        except ValueError:
            print('Please enter a number only.')
            milk_request = int(input())
        while 0 > milk_request > 1:
            print('Please enter a 0 or 1 only:')
            try:
                milk_request = int(input())
            except ValueError:
                print('Please enter a 0 or 1 only:')
                milk_request = int(input())
        # Ask for sugar:
        print('Would you like to add sugar to your beverage?')
        print('  [0] No')
        print('  [1] Yes')
        try:
            sugar_request = int(input())
        except ValueError:
            print('Please enter a number only.')
            sugar_request = int(input())
        while sugar_request < 0 or sugar_request > 1:
            print('Please enter a 0 or 1 only:')
            try:
                sugar_request = int(input())
            except ValueError:
                print('Please enter a 0 or 1 only:')
                sugar_request = int(input())

        # Define max units of condiments allowed
        user_units_milk = 0
        user_units_sugar = 0
        max_units = 3

        # If milk desired, ask for how much milk:
        if milk_request == 1:
            print('How many units of milk?')
            user_units_milk = int(input())
            user_condiments = Condiments(units_milk=user_units_milk)

        # If sugar desired, ask for how much sugar:
        if sugar_request == 1:
            print('How many units of sugar?')
            user_units_sugar = int(input())
            user_condiments = Condiments(units_sugar=user_units_sugar)

        # Validate that condiments are <= 3 units. Else restart condiment request.
        condiment_units_requested = user_units_milk + user_units_sugar
        print(f'\nYour condiment selection:')
        print(f'{user_condiments.confirm_condiments()}')
        if condiment_units_requested > 3:
            print()
            print('Oops, too many condiment units specified.')
            print('Please try again:')
            print()
            UserInterface.ask_condiments()

    def close_order():
        print('\nEnjoy your beverage!')
