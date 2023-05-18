#  File: LeftSum.py
#  Description: Get the left sum of the BST
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020


import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    # insert data into the tree
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        else:
            current = self.root
            parent = self.root
            while current is not None:
                parent = current
                if data < current.data:
                    current = current.lchild
                else:
                    current = current.rchild

            # found location now insert node
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node

    # Returns an integer for the left sum of the BST
    def get_left_sum(self):
        if self.root is None:
            return None

        left_side = []                            # store values of the left-side view
        q = Queue()                               # create a queue
        q.enqueue(self.root)                      # enqueue the root

        while not q.is_empty():                   # while queue is not empty,
            level_size = q.size()                 # record the number of nodes on the current level of BST
            left_node = q.queue[0].data           # first node of level is left-side view node
            left_side.append(left_node)           # append left-side view node to left_side list

            for i in range(level_size):           # traverse the current BST level
                current = q.dequeue()             # current node being explored

                if current.lchild:
                    q.enqueue(current.lchild)     # enqueue the current node's left child, if exists
                if current.rchild:
                    q.enqueue(current.rchild)     # enqueue the current node's right child, if exists

        left_sum = sum(left_side)                 # entire tree has been traversed. calculate sum of left nodes.

        return left_sum                           # return left sum


def main():
    # Create tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list(map(int, line))  # converts elements into ints

    tree = Tree()
    for i in tree_input:
        tree.insert(i)

    print(tree.get_left_sum())


if __name__ == "__main__":
    main()
