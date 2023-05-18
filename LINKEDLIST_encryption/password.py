#  File: password.py
#  Description: Rotates a linked list to the left (counter-clockwise) r_step times 
#  Student Name: Raquel Mejia-Trujillo
#  Student UT EID: rm57578
#  Course Name: CS 313E
#  Unique Number: 52020

import copy


class Link:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None

    def insert_last(self, data):
        newLink = Link(data)
        current = self.first

        if current is None:
            self.first = newLink
            return

        while current.next is not None:
            current = current.next

        current.next = newLink

    # helper function to copy the contents of the current linked list
    # returns new linked list
    def copy_list(self):
        new_list = LinkedList()
        curr = self.first
        while curr:
            new_list.insert_last(curr.data)
            curr = curr.next
        return new_list

    # helper function to count number of links
    # returns number of links
    def num_links(self):
        curr = self.first
        res = 0
        while curr:
            res += 1
            curr = curr.next
        return res

    # string representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        curr_items = []
        curr = self.first
        res = ""
        while curr:
            curr_items.append(curr.data)
            if len(curr_items) == 10:
                res += "  ".join(map(str, curr_items)) + "\n"
                curr_items = []
            curr = curr.next
        # print the remaining items
        if len(curr_items):
            res += "  ".join(map(str, curr_items))
        return res

    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current is None:
            return None

        while current.data != data:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # return a new linked list that results from the rotation
    def rotate(self, r_step, times):
        password = copy.deepcopy(self)  # copy of self so self can be printed later

        for _ in range(times):          # user specifies number of times to repeat the rotation of the linked list
            current = password.first    # current is the first in linked list
            steps = 0

            # rotate counter-clockwise r_step times as long as we are not at end of linked list and next exists
            while steps < (r_step - 1) \
                    and current is not None \
                    and current.next is not None:
                current = current.next
                steps += 1

            temp = current  # temp keeps track of last arrangement of linked list before needing to re-assign `first`

            # if previous rotations didn't reach the end of the list,
            # continue rotating counter-clockwise until we reach the end of the linked list
            while current.next is not None:
                current = current.next

            current.next = password.first  # move the first element of initial linked list to the end
            password.first = temp.next     # update the password one position after the arrangement that we left off at
            temp.next = None

        # return the password
        return password


def main():
    ll = LinkedList()

    data = list(map(int, input().split()))

    # populate linked list with data
    for d in data:
        ll.insert_last(d)

    r_step, times = list(map(int, input().split()))

    rotated = ll.rotate(r_step, times)
    # print the original list
    print(ll)
    # print the new list that results from calling rotate()
    print(rotated)


if __name__ == "__main__":
    main()
