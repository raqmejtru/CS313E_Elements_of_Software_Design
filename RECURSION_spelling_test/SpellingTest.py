#  File: SpellingTest.py
#  Description: Given a string s and a list of strings l, determine whether s can be spelled by some combination of
#               strings in l, using each string in l no more than once.
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020

import sys


def spelling_test(s, l):

    if len(s) == 0:
        # if all letters in s have been deleted,
        # then s can be spelled by some combination of strings in l, using each string in l no more than once.
        return True

    if len(l) == 0 and len(s) > 0:
        # if all substrings searched and s is not completely deleted
        # then s cannot be spelled by combination of strings in l, using each string in l no more than once.
        return False

    if l[0] not in s:  # if current substring not in s
        l.pop(0)       # remove current substring from list
        return spelling_test(s, l)  # repeat

    if l[0] in s:                   # if current substring in s
        s = s.replace(l[0], '')     # delete current substring from s
        l.pop(0)                    # remove current substring from list, since can only be used once.
        return spelling_test(s, l)  # repeat


def main():
    s = input()
    lines = sys.stdin.readlines()
    print(spelling_test(s, [line.replace('\n', '') for line in lines]))


if __name__ == "__main__":
    main()
