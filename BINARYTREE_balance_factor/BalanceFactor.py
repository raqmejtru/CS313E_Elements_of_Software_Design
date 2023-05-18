#  File: BalanceFactor.py
#  Description: Determines the balance factor of a binary tree
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020


import pickle
import sys


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Returns the height of a tree rooted at the given node
def get_height(node):
    if node is None:
        return 0

    return 1 + max(get_height(node.left), get_height(node.right))


# Returns the integer balance factor of a tree rooted at the given node.
def balance_factor(node):
    if node is None:
        return 0

    l = 0  # default left subtree height
    r = 0  # default right subtree height

    if node.left:                   # If left node exists,
        l = get_height(node.left)   # compute the height of left subtree.

    if node.right:                  # If right node exists,
        r = get_height(node.right)  # compute the height of the right subtree.

    return r - l  # Return the balance factor


def main():
    data_in = ''.join(sys.stdin.readlines())
    node = pickle.loads(str.encode(data_in))

    print(balance_factor(node))


if __name__ == "__main__":
    main()
