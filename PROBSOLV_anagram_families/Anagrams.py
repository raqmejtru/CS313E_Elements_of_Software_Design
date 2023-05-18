# File: Anagrams.py
# Description: A program to group strings into anagram families
# Student Name: Raquel Mejia-Trujillo
# Course Name: CS 313E
# Unique Number: 52020

# Output: True or False
def are_anagrams(str1, str2):
    # Sorted lists ok, since inputs are all lowercase letters
    letters_1 = [letter for letter in str1]
    letters_1 = sorted(letters_1)
    letters_2 = [letter for letter in str2]
    letters_2 = sorted(letters_2)

    # Anagrams must be the same length
    # Checking length accounts for anagrams that may have repeated letters
    if not len(letters_1) == len(letters_2):
        return False
    else:
        # If ordered sets are identical, two words are considered anagrams
        set_1 = set(letters_1)
        set_2 = set(letters_2)
        if set_1 == set_2:
            return True


# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    # Outline:
    # 1. Dictionary keys are str of the ordered set(letters) of each word
    # 2. Dictionary values are a list of word(s) that are anagrams
    # 3. Number of keys is number of anagram families

    # Initiate empty dictionary
    families = dict()

    for word in lst:
        # Check if word has anagram in list
        word_has_anagram = False
        for i in range(0, len(lst)):
            if are_anagrams(word, lst[i]):
                word_has_anagram = True

        if word_has_anagram:
            # Create the (unique) anagram_key
            potential_anagram_letters = sorted([letter for letter in word])
            # Keys cannot be lists, so join letters into string
            anagram_key = "".join([str(i) for i in potential_anagram_letters])

            # If anagram_key already exists, append word to the values
            if anagram_key in families.keys():
                families[anagram_key].append(word)
            # Else create new list of potential words that are anagram families
            else:
                families[anagram_key] = [word]

    # Return the number of anagram families (number of keys)
    return len(families)


def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)


if __name__ == "__main__":
    main()
