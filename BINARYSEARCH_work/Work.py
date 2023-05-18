#  File: Work.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 02/23/2023
#  Date Last Modified: 02/27/2023


import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series ((v) + (v // k) + (v // k**2) + ...)
#         returns the sum of the series
def sum_series(v, k):
    n_i = 1                     # Initiate n_i with 1. Overwritten when loop is initiated.
    n_total = 0                 # Zero lines of code written when function initiates
    k_power = 0                 # k is first raised to the power of 0

    # Compute sum of series.
    while n_i > 0:              # When n_i is zero, falls asleep, no more lines of code written.
        n_i = v // k**k_power
        n_total += n_i
        k_power += 1

    # Return the total number of lines of code that can be written given parameters v, k
    return n_total


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search(n, k):
    v = 0
    n_total = 0

    while n_total < n:
        # While v is too small, increment v by 1.
        v += 1
        # Compute n for current value of v
        n_total = sum_series(v, k)

    # Return the minimum value of v for a given k that accomplishes writing at least n lines of code
    return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n, k):
    # Starting value of v is the closest midpoint of n, since all possible
    # final values of v will be greater than the midpoint of n
    minimum = n // 2
    maximum = n
    v = None

    # Binary search procedure
    while minimum <= maximum:
        v = (minimum + maximum) // 2
        n_total = sum_series(v, k)

        if n_total < n:
            # If sum_series output is too small, try incrementing v by 1 first
            # If sum_series output of v + 1 is > n, then v + 1 is the minimum value of v
            if sum_series(v + 1, k) > n:
                return v + 1
            # Otherwise, define new minimum search range if sum_series output is too small
            else:
                minimum = v + 1

        elif n_total > n:
            # Define new maximum search range if sum_series output is too large
            maximum = v - 1

        elif n_total == n:
            # If sum_series output is n, v is the minimum value of v
            break

    # Return the minimum value of v for a given k that accomplishes writing at least n lines of code
    return v


def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        # Compare binary and linear search times:
        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()
