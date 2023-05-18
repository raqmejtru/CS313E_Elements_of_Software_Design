#  File: maximum_profit.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 04/17/2023
#  Date Last Modified: 04/17/2023


import sys


def print_memo(memo: list):
    for row in memo:
        print(row)


def get_memo(max_price: int, num_houses: int, prices: list, forecasted_increases: list) -> list:
    
    # Generate memoization table to track current max profit
    n_rows = num_houses + 1
    n_cols = max_price + 1
    memo = [[0 for col in range(n_cols)] for row in range(n_rows)]

    # Loop through all rows and cols of the memoization table to consider all possible purchase combinations.
    for house in range(1, n_rows):
        for total_price in range(1, n_cols):

            #  If price of previous house is less than the price of the current purchase combination,
            if prices[house - 1] <= total_price:

                # opt_1: add the increase from the previous house to the current increase, given the house is purchased.
                opt_1 = forecasted_increases[house - 1] + memo[house - 1][total_price - prices[house - 1]]

                # opt_2: keep the current purchase combination, without purchasing the previous house.
                opt_2 = memo[house - 1][total_price]

                # keep the maximum forecasted increase of opt_1 and opt_2
                memo[house][total_price] = max(opt_1, opt_2)

            else:
                # otherwise, if the price of previous house is more than the current purchase combination,
                # keep the current total forecasted increase.
                memo[house][total_price] = memo[house - 1][total_price]

    return memo


# Find the maximum profit by identifying which combination of houses were purchased.
def get_profit(memo: list, max_price: int, num_houses: int, prices: list, forecasted_increases: list) -> float:

    current = memo[num_houses][max_price]      # Set starting value as the bottom right element of memoization table
    profit = 0                                 # Set the initial profit to zero

    # Backtrack through memoization table
    for house in range(num_houses, 0, -1):

        # If the forecasted increase did not change when a new house was taken into consideration, continue.
        if current == memo[house - 1][max_price]:
            continue

        # Otherwise, the house should be purchased and taken into consideration for profit.
        else:
            include_p = prices[house - 1]                 # price of current house
            include_i = forecasted_increases[house - 1]   # forecasted increase of current house

            profit += (include_p * include_i)             # add forecasted profit (price * forecasted increase)

            max_price -= prices[house - 1]                # subtract cost of purchasing the house
            current -= forecasted_increases[house - 1]    # subtract forecasted increase of the house

    profit /= 100   # divide by 100 to convert to decimal
    return profit   # return profit


def main():

    # The first line is the amount of investment in millions of USD, which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    max_price = int(line)

    # The second line is the number of houses listed for sale, which is an integer.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    # The third line is a list of house prices in millions of dollars, which is a list of integers.
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])

    # The fourth line is a list of 1-year forecasted_increases for each of the listed houses in percents.
    line = sys.stdin.readline()
    line = line.strip()
    forecasted_increases = line.split(",")
    for i in range(0, len(forecasted_increases)):
        forecasted_increases[i] = int(forecasted_increases[i])

    memo = get_memo(max_price, num_houses, prices, forecasted_increases)
    result = get_profit(memo, max_price, num_houses, prices, forecasted_increases)
    print(result)


if __name__ == '__main__':
    main()
