"""
This program runs a fully automatic beverage machine.
CS313E
01/26/2023
Raquel Mejia
"""


import os
import time
from interface import UserInterface


# To clear terminal screen (adapted from K.T. GitHub)
def clear_screen(sec):
    print("Ordering interface will close in " + str(sec) + " seconds. ")
    time.sleep(sec)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    run = True
    while run:
        UserInterface.show_menu()
        UserInterface.user_selection()
        UserInterface.ask_condiments()
        UserInterface.close_order()
        print('Do you want to place another order?')
        print('  [0] No')
        print('  [1] Yes')
        try:
            repeat = int(input())
        except ValueError:
            print('Please enter a number only.')
            repeat = int(input())
        while repeat < 0 or repeat > 1:
            print('Please enter a 0 or 1 only:')
            try:
                repeat = int(input())
            except ValueError:
                print('Please enter a 0 or 1 only:')
                repeat = int(input())
        if repeat == 0:
            run = False
    clear_screen(5)


if __name__ == "__main__":
    main()
