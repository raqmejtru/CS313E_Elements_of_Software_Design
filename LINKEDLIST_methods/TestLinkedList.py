#  File: TestLinkedList.py
#  Description: Write helper methods for the LinkedList class
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020

import random


class Link:
    # constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None

    # Get number of links of a singly Linked List. ---------------------------------------------------------------------
    # "Input: [1, 2, 3, 4, 5, 6]"
    # "Expected: 6"
    def get_num_links(self):
        current = self.first
        count = 1

        # rotate through list until end is reached, keep track of number of rotations.
        while current is not None and current.next is not None:
            count += 1
            current = current.next

        return count

    # Add an item at the beginning of the list -------------------------------------------------------------------------
    def insert_first(self, data):
        new = Link(data)       # create new link
        new.next = self.first  # append linked list to the end of the new link
        self.first = new       # re-assign self as the new link

    # Add an item at the end of a list ---------------------------------------------------------------------------------
    def insert_last(self, data):
        new = Link(data)       # create new link
        current = self.first

        if current is None:    # if linked list is empty
            self.first = new   # new link is the first item
            return

        # otherwise rotate through list until end is reached
        while current.next is not None:
            current = current.next

        # append the new link to the end of the linked list
        current.next = new
        return current

    # Add an item in an ordered list in ascending order ----------------------------------------------------------------
    # Assume that the list is already sorted
    def insert_in_order(self, data):
        new = Link(data)
        current = self.first

        if current is None:         # if linked list is empty
            self.insert_first(data) # insert first
            return

        if current.data > data:     # if first > data
            new.next = self.first   # data should be the new first element
            self.first = new
            return

        # otherwise rotate through the list and find the position prior to the given data
        while current.next is not None and current.next.data < data:
            current = current.next

        new.next = current.next
        current.next = new
        return

    # Search in an unordered list, return None if not found ------------------------------------------------------------
    def find_unordered(self, data):
        current = self.first
        if current is None:
            return None

        # rotate through the list until data is found (otherwise return None)
        while current.data != data:
            if current.next is None:
                return None
            else:
                current = current.next

        return current # return link

    # Search in an ordered list, return None if not found --------------------------------------------------------------
    def find_ordered(self, data):
        current = self.first
        if current is None:
            return None

        # rotate through the list until data is found/current value is greater than data/reach end of list
        while current.data <= data:
            if current.next is None:      # data is larger than max value of list
                return None
            if current.data == data:      # current data is data! found.
                return current            # return link
            if current.next.data > data:  # next value is > data. stop searching.
                return None
            else:
                current = current.next

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        string = ""
        count = 0
        curr = self.first
        if curr is None:
            return string

        while curr.next is not None:
            string += str(curr.data)
            count += 1
            if count != 30:
                string += "  "
            else:
                string += "\n"
                count = 0
            curr = curr.next
        string += str(curr.data)
        return string


# This main function is for visualization and tests.
def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    linked_List = LinkedList()
    linked_List.insert_in_order(2)
    linked_List.insert_in_order(5)
    linked_List.insert_in_order(7)
    linked_List.insert_in_order(8)
    linked_List.insert_in_order(6)

    print('linked_List', linked_List)

    # Test method insert_last()
    linked_List.insert_last(10)
    print('insert_last:', linked_List)

    # Test method insert_in_order()
    # linked_List.insert_in_order(0)
    print('insert_in_order', linked_List)

    # Test method get_num_links()
    num_links = linked_List.get_num_links()
    print('num_links:', num_links)

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print(linked_List.find_unordered(3))
    print(linked_List.find_unordered(11))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print(linked_List.find_ordered(6))
    print(linked_List.find_ordered(12))


if __name__ == "__main__":
    main()
