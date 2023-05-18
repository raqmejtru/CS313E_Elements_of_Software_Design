#  File: reward.py
#  Description: The ABC staff decides to find the minimum number of gifts as each customer's reward.
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020

import sys

max_val = 1000


def getmin(prices, T):
    # Generate memoization table
    gift_price = round(T * 0.1)
    num_gifts = len(prices)
    memo = [[0 for col in range(gift_price + 1)] for row in range(num_gifts)]

    # Increment first row based on the number of gifts that can be purchased
    # by repeatedly buying the first gift, while staying within the gift budget.
    for num_first_gift in range(gift_price + 1):
        if num_first_gift % prices[0] == 0:
            memo[0][num_first_gift] = num_first_gift // prices[0]
        else:
            memo[0][num_first_gift] = max_val

    # Loop through remaining rows to consider all possible gift combinations.
    for gift in range(1, num_gifts):
        for total_price in range(gift_price + 1):
            opt_1 = memo[gift - 1][total_price]  # Previous number of gifts
            opt_2 = max_val                      # Dummy number that will always be > previous num of gifts

            # If current gift price is below the gift budget,
            if prices[gift] <= total_price:
                # Update num of gifts to include the current gift, given that the price is deducted from budget.
                opt_2 = 1 + memo[gift][total_price - prices[gift]]

            # Keep the minimum number of gifts between opt_1 and opt_2
            memo[gift][total_price] = min(opt_1, opt_2)

    min_num_gifts = memo[num_gifts - 1][gift_price]

    # Return -1 if we cannot find gifts worthy of the reward program
    if min_num_gifts >= max_val:
        return -1

    # Otherwise return the minimum number of gifts that the customer will receive
    return min_num_gifts

def main():
    # Read input list of prices for each gift
    prices_str = sys.stdin.readline().split()
    prices = [int(x) for x in prices_str]

    # Read total price that the customer spends
    T = int(sys.stdin.readline())

    print(getmin(prices, T))

if __name__ == "__main__":
    main()
