#  File: toomany.py
#  Description: Each flower has to be inserted into one of the vases.
#				She wants to arrange the flower so that no more than two flowers of the same type
#				will be inserted in the same vase.
#				She wants to find out which type of flower will be left after her arrangement.
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020

import sys


# Input: flower_list is a list of integers that represent the flower type.
#		 N is the number of vases
# Output: is a list of flower types that Jennifer bought too many (sorted)
def findTooMany(flower_list: list, N: int):
	# Possible flowers number 1 to 9

	fl_set = set(flower_list)                                  # set of flower types
	fl_dict = {key: flower_list.count(key) for key in fl_set}  # flower type:total count of type
	vases = {key: [] for key in range(N)}                      # vase: empty list of flowers in vase

	vase_key = 0
	for fl_key, fl_count in fl_dict.items():  # For each flower type,
		vases[vase_key].append(fl_key)        # Add 1 flower to vase
		fl_dict[fl_key] -= 1                  # Subtract 1 from flower counts, since flower was added to vase.

	fl_dict = {key: val for key, val in fl_dict.items() if val > 0}  # Update dict: only include types with count > 0

	if len(fl_dict) == 0:  # If all available flowers have been put in a vase, return empty list.
		return []

	# Otherwise continue adding flowers to a vase until it reaches limit of 2 of one type of flower:
	remaining = max([val for val in fl_dict.values()])      # Total number of remaining flowers
	while remaining > 0 and vase_key < N:                   # While flowers remain and vases remain to be searched
		for fl_key, fl_count in fl_dict.items():            # Loop through each unique flower type
			num_duplicates = vases[vase_key].count(fl_key)  # Count the number of current flower type already in vase
			if num_duplicates < 2:                          # As long as there is only 1 of that flower type in vase,
				vases[vase_key].append(fl_key)              # Add the current flower to the vase
				fl_dict[fl_key] -= 1                        # Subtract from flower count
				remaining = max([val for val in fl_dict.values()])  # Update number of remaining flowers
			else:
				break

		vase_key += 1  # Current vase reached limit of 2 of one type of flower, move to next vase.
		fl_dict = {key: val for key, val in fl_dict.items() if val > 0}  # Update dict: only include types with count > 0

	too_many = [key for key in fl_dict.keys()]  # Types of leftover flowers
	return too_many

def main():
	# Read flower_list
	flower_list_str = sys.stdin.readline().split()
	flower_list = [int(x) for x in flower_list_str]

	# N: number of vases
	N = int(sys.stdin.readline())

	# output list of flower types. sorted.
	item_too_many_ls = findTooMany(flower_list, N)

	print(item_too_many_ls)

if __name__ == '__main__':
	main()
	