#  File: Interval.py
#  Description: A basic interval class.
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020

import sys


class IntegerInterval(object):
    # constructor with default values
    def __init__(self, beginning=0, end=0):
        # User can specify:
        self.beginning = int(beginning)
        self.end = int(end)
        # Exclusive interval:
        self.interval = {int(i) for i in range(self.beginning + 1, self.end)}

    # creates a string representation of an Interval
    # returns a string in the form "Beginning: startTime, End: endTime"
    def __str__(self):
        return f'Beginning: {self.beginning}, End: {self.end}'

    # test for equality between two intervals
    # other is an interval object
    # returns a Boolean
    def __eq__(self, other):
        if self.beginning == other.beginning and self.end == other.end:
            return True
        else:
            return False

    # returns the length of this interval
    # returns an integer 
    def __len__(self):
        length = self.end - self.beginning
        return length

    # determine if this interval overlaps with another
    # other is an interval object
    # returns a Boolean
    def overlap(self, other):
        if self == other:
            return True
        elif self.beginning in other.interval or self.end in other.interval:
            return True
        elif other.beginning in self.interval or other.end in self.interval:
            return True
        else:
            return False

    # determine the time in the intersection of this interval with another
    # other is an interval object
    # returns an Integer
    def intersection(self, other):
        if not self.overlap(other):
            # No intersection, intersection_time is 0
            return 0
        else:
            intersection_time = min(self.end, other.end) - max(self.beginning, other.beginning)
            return intersection_time

    # determine the time in the union of this interval with another
    # other is an interval object
    # returns an Integer
    def union(self, other):
        union_time = len(self) + len(other) - self.intersection(other)
        return union_time


def main():
    # read the two intervals
    line1 = sys.stdin.readline()
    line2 = sys.stdin.readline()
    line1 = line1.split(" ")
    line2 = line2.split(" ")

    interval1 = IntegerInterval(int(line1[0]), int(line1[1]))
    interval2 = IntegerInterval(int(line2[0]), int(line2[1]))

    # print the output
    print(interval1)
    print(interval2)
    print(len(interval1))
    print(len(interval2))
    print(interval1 == interval2)
    print(interval1.overlap(interval2))
    print(interval2.overlap(interval1))
    print(interval1.intersection(interval2))
    print(interval2.intersection(interval1))
    print(interval1.union(interval2))
    print(interval2.union(interval1))


if __name__ == "__main__":
    main()
