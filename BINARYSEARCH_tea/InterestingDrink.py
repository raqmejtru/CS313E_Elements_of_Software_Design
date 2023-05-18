#  File: InterestingDrink.py
#  Description: Implement find_purchase_options function that given a list of integers named prices that contains
#               the price of black tea in each store, and a list of integers named money that contains the amount of money
#               Tim will spend in a given day, returns a list of integers representing how many different shops
#               Tim can buy a cup of black tea.
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020

import sys


# A binary search implementation
def binary_search(lst, x):
    low = -1
    high = len(lst)
    while low < high - 1:
        middle = (low + high) // 2
        if lst[middle] <= x:
            low = middle
        else:
            high = middle

    # return index of x in lst
    return low


# Input: prices a list of integers containing the price of black tea in each store
#        money  a list of integers containing the amount of money Tim will spend in a given day
# Returns: a list of integers representing how many different shops Tim can buy a cup of black tea.
def find_purchase_options(prices, money):
    prices_sorted = sorted(prices)

    lst_num_stores = []
    for daily_max in money:
        # Find index of daily_max in prices_sorted list
        index = binary_search(prices_sorted, daily_max)

        # Find the length of the sublist of prices that are within daily max budget
        prices_lt_or_eq_max = prices_sorted[0:index + 1]
        lst_num_stores.append(len(prices_lt_or_eq_max))

    return lst_num_stores


#######################################################################################################
# The input format from the main is two lines, each line contains some integers split by a single space.
# For example:
# 3 10 8 6 11
# 1 10 3 11
#######################################################################################################
def main():
    # Read the prices list
    prices = [*map(int, sys.stdin.readline().split())]
    # Read the money list
    money = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = find_purchase_options(prices, money)
    sys.stdout.write(f'Result by calling find_purchase_option {ans}')


if __name__ == '__main__':
    main()
