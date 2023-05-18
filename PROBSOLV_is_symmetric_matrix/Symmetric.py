#  File: Symmetric.py
#  Description: Determines if a square 2d list of 1s and 0s has some "symmetry" where the matrix is
#               the same as its transpose
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020


# Prints 2D list, for debugging purposes
def print_arr(temp):
    mx = max((len(str(ele)) for sub in temp for ele in sub))
    for row in temp:
        print(" ".join(["{:<{mx}}".format(ele, mx=mx) for ele in row]))
    print()


# Input: matrix is a 2d square list of 1s and 0s
# Output: return True if the matrix is equal to its transpose (rows and columns swapped)
# return False otherwise
def matrix_has_symmetry(matrix):
    # Define dimension of square matrix
    n = len(matrix)

    # Create empty n x n matrix_t, the transpose of matrix
    matrix_t = [[None for i in range(n)] for j in range(n)]

    # Fill in matrix_t
    for row in range(n):
        for col in range(n):
            matrix_t[col][row] = matrix[row][col]

    # If matrix is symmetric (equal to its transpose), return true, else return false
    if matrix == matrix_t:
        return True
    else:
        return False


def main():
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to matrix_has_symmetry()
    result = matrix_has_symmetry(matrix)

    # print the result to standard output
    print(result)


if __name__ == "__main__":
    main()
