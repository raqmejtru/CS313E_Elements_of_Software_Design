#  File: Spiral.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 01/20/2023
#  Date Last Modified: 01/23/2023

import sys


# Input:  n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    # Confirm that n is odd. If not, add 1 to n:
    n = n + 1 if (n % 2 == 0) else n

    # Initiate an n x n dimensional list:
    matrix = [[0 for i in range(n)] for j in range(n)]

    # Define the center of the matrix as the start of the spiral:
    center = n // 2
    row, col = center, center

    # Assign the center of the matrix with value 1:
    matrix[row][col] = 1

    # Define the total number of direction changes needed to complete the spiral:
    # (Note: does not include the final direction change on top row)
    total_direction_changes = (n * 2) - 2

    # Define variables that will be used in while loop:
    # First value that is assigned after the center of the spiral (value 1)
    new_value = 2
    # Tracks number of times to continue assigning values in one direction        
    repeat_count = 1
    # Tracks number of times that direction changes while moving in spiral     
    direction_change = 0

    # Fill in spiral -----------------------------------------------------------
    # Each `for` loop performs the following:
    # 1. Moves a current position within a matrix a particular direction
    # 2. Assigns the updated position with an incremental value
    # 3. Repeats this process a designated number of times 

    while direction_change < total_direction_changes:
        # Right -------------------------------------
        for x in range(repeat_count):
            col += 1
            matrix[row][col] = new_value
            new_value += 1
        direction_change += 1

        # Down --------------------------------------
        for x in range(repeat_count):
            row += 1
            matrix[row][col] = new_value
            new_value += 1
        direction_change += 1
        repeat_count += 1

        # Left --------------------------------------
        for x in range(repeat_count):
            col -= 1
            matrix[row][col] = new_value
            new_value += 1
        direction_change += 1

        # Up ----------------------------------------
        for x in range(repeat_count):
            row -= 1
            matrix[row][col] = new_value
            new_value += 1
        direction_change += 1
        repeat_count += 1

        # Compared to other iterations, the final top row requires 
        # one less repeat of the `for` loop moving right:
        if direction_change == total_direction_changes:
            repeat_count -= 1
            for x in range(repeat_count):
                col += 1
                matrix[row][col] = new_value
                new_value += 1
            break

    return matrix


# Input: spiral is a 2-D list and number is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to number in the spiral;
#         if number is outside the range return 0.
def sum_adjacent_numbers(matrix, number):
    # If number does not exist in matrix, return 0.  
    if not any(number in row for row in matrix):
        return print(0)
    else:
        # Which values in which corners? 
        max_index = len(matrix) - 1
        TL = matrix[0][0]
        TR = matrix[0][max_index]
        BL = matrix[max_index][0]
        BR = matrix[max_index][max_index]

        # Which values along edges?
        top = matrix[0]
        bottom = matrix[max_index]
        left = [row[0] for row in matrix]
        right = [row[max_index] for row in matrix]

        # Identify location of number. 
        for row in matrix:
            if number in row:
                row_index = matrix.index(row)
                row_contents = matrix[row_index]
        for col in row_contents:
            if number == col:
                col_index = row_contents.index(col)

        # If at corner, only sum three adjacent values.
        if number == TL:  # Top left
            total_sum = matrix[0][1] + matrix[1][0] + matrix[1][1]
            return print(total_sum)
        elif number == TR:  # Top right
            total_sum = matrix[0][max_index - 1] + matrix[1][max_index - 1] + matrix[1][max_index - 1]
            return print(total_sum)
        elif number == BL:  # Bottom left
            total_sum = matrix[max_index - 1][0] + matrix[max_index - 1][1] + matrix[max_index][1]
            return print(total_sum)
        elif number == BR:  # Bottom right
            total_sum = matrix[max_index - 1][max_index] + \
                        matrix[max_index][max_index - 1] + \
                        matrix[max_index - 1][max_index - 1]
            return print(total_sum)

        # If number on edges, return sum of five adjacent values. 
        elif number in left:
            total_sum = matrix[row_index - 1][col_index] + \
                        matrix[row_index - 1][col_index + 1] + \
                        matrix[row_index][col_index + 1] + \
                        matrix[row_index + 1][col_index + 1] + \
                        matrix[row_index + 1][col_index]
            return print(total_sum)
        elif number in right:
            total_sum = matrix[row_index - 1][col_index] + \
                        matrix[row_index - 1][col_index - 1] + \
                        matrix[row_index][col_index - 1] + \
                        matrix[row_index + 1][col_index - 1] + \
                        matrix[row_index + 1][col_index]
            return print(total_sum)
        elif number in top:
            total_sum = matrix[row_index][col_index - 1] + \
                        matrix[row_index][col_index + 1] + \
                        matrix[row_index + 1][col_index - 1] + \
                        matrix[row_index + 1][col_index] + \
                        matrix[row_index + 1][col_index + 1]
            return print(total_sum)
        elif number in bottom:
            total_sum = matrix[row_index][col_index - 1] + \
                        matrix[row_index][col_index + 1] + \
                        matrix[row_index - 1][col_index - 1] + \
                        matrix[row_index - 1][col_index] + \
                        matrix[row_index - 1][col_index + 1]
            return print(total_sum)

        # Otherwise, return sum of all eight adjacent values. 
        else:
            sum_top = matrix[row_index - 1][col_index - 1] + \
                      matrix[row_index - 1][col_index] + \
                      matrix[row_index - 1][col_index + 1]
            sum_same_row = matrix[row_index][col_index - 1] + matrix[row_index][col_index + 1]
            sum_bottom = matrix[row_index + 1][col_index - 1] + \
                         matrix[row_index + 1][col_index] + \
                         matrix[row_index + 1][col_index + 1]
            total_sum = sum_top + sum_same_row + sum_bottom
            return print(total_sum)


def main():
    # Read standard input file
    in_file = sys.stdin.read()
    in_list = in_file.split('\n')

    # Convert inputs to integers
    for i in range(len(in_list)):
        if in_list[i] != '':
            in_list[i] = int(in_list[i])
        else:
            in_list.remove(in_list[i])

    # Define spiral dimension
    n = in_list.pop(0)

    # Create spiral
    matrix = create_spiral(n)

    # Add the adjacent numbers and print results
    for number in in_list:
        sum_adjacent_numbers(matrix, number)


if __name__ == "__main__":
    main()
