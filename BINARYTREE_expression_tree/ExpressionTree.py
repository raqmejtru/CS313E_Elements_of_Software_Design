#  File: ExpressionTree.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 03/20/2023
#  Date Last Modified: 03/20/2023


import sys


operators = ['+', '-', '*', '/', '//', '%', '**']
postfix_list = []
prefix_list = []


class Stack:
    def __init__(self):
        self.stack = []

    def print(self):
        print(self.stack)

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print_node(self, level=0):
        if self.right is not None:
            self.right.print_node(level + 1)

        print(' ' * 4 * level + '->', self.data)

        if self.left is not None:
            self.left.print_node(level + 1)

    # Traversal: left, center, right
    # Appends data to prefix_list in traversal order
    def LCR(self, node):
        global prefix_list
        if node is not None:
            prefix_list.append(node.data)
            node.LCR(node.left)
            node.LCR(node.right)

    # Traversal: left, right, center
    # Appends data to postfix_list in traversal order
    def LRC(self, node):
        global postfix_list
        if node is not None:
            node.LRC(node.left)
            node.LRC(node.right)
            postfix_list.append(node.data)


class Tree:
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree(self, expr):
        token_ls = expr.split()
        temp_stack = Stack()
        self.root = Node()
        current = self.root

        for token in token_ls:
            if token == '(':
                temp = Node()
                current.left = temp
                temp_stack.push(current)
                current = current.left

            elif token == ')':
                if temp_stack.is_empty() is False:
                    current = temp_stack.pop()

            elif token in operators:
                current.data = token
                temp_stack.push(current)
                temp = Node()
                current.right = temp
                current = current.right

            else:
                current.data = token
                current = temp_stack.pop()

    # Prints expression tree
    def print(self, level):
        self.root.print_node(level)

    # Returns height of expression tree
    # Used to define `level` for print method
    def height(self):
        if self.root is None:
            return 0

        # Left height
        current = self.root
        n_min = -1
        while current is not None:
            current = current.left
            n_min += 1

        # Right height
        current = self.root
        n_max = -1
        while current is not None:
            n_max += 1
            current = current.right

        # Return max of left and right height
        height = max(n_min, n_max)
        return height

    # evaluate the tree's expression,
    # returns the value of the expression after being calculated
    def evaluate(self):
        # Create postfix_list if the list has not been created yet
        if len(postfix_list) == 0:
            self.root.LRC(self.root)

        eval_stack = Stack()  # Empty stack that will hold current operations
        temp = postfix_list  # Temporary list to know when all values in postfix_list have been traversed
        while len(temp) > 0:
            current = temp.pop(0)  # Current operand or operator.
            if current not in operators:  # If current is an operand,
                eval_stack.push(current)  # then push operand to eval_stack.
            else:  # Otherwise, current is operator.
                operand_2 = eval_stack.pop()  # Top of eval_stack is operand_2
                operand_1 = eval_stack.pop()  # New top of eval_stack is operand_1
                operator = current
                result = eval(f'{operand_1} {operator} {operand_2}')  # Evaluate expression
                eval_stack.push(result)  # Push result to the tree, repeat until expression is fully evaluated.

        return float(result)  # Return final result of expression

    # generate the preorder notation of the tree's expression,
    # returns a string of the expression written in preorder notation
    def pre_order(self):
        # Creates list by traversing through tree: left, center, right
        self.root.LCR(self.root)
        return prefix_list

    # generate the postorder notation of the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self):
        # Creates list by traversing through tree: left, right, center
        self.root.LRC(self.root)
        return postfix_list


def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)
    prefix_expression = ' '.join(tree.pre_order())
    postfix_expression = ' '.join(tree.post_order())

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate()))

    # get the prefix version of the expression and print
    print("Prefix Expression:", prefix_expression)

    # get the postfix version of the expression and print
    print("Postfix Expression:", postfix_expression)


if __name__ == "__main__":
    main()
