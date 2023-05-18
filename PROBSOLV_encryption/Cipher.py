#  File: Cipher.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 01/27/2023
#  Date Last Modified: 01/27/2023


import math


# Input: `p` is a string of 100 or less of upper case, lower case, and digits
# Output: function returns an encrypted string 
def encrypt(p):
	# Define length of string p
	length = len(p)

	# Exit if string is too long
	if length > 100:
		print('String is too long. Must be < 100 characters.')
		pass
	else:
		# Define smallest n x n matrix that can accommodate all values of p
		root = math.sqrt(length)
		n = math.ceil(root)

		# Add asterisks to string p, if n x n matrix has empty elements.
		asterisks_needed = (n * n) - length
		p = p + asterisks_needed * '*'
		p_list = list(p)

		# Initialize empty n x n matrix `m`
		m = [[None for i in range(n)] for j in range(n)]

		# Fill in matrix `m` in row-major order
		for row in range(n):
			m[row] = p_list[0:n]
			if row != n - 1:
				# Remove elements that have already been filled into `m`
				for element in range(n):
					p_list.pop(0)

		# Create matrix `m_t`, the transpose of `m`.
		m_t = [[None for i in range(n)] for j in range(n)]
		for row in range(n):
			for col in range(n):
				m_t[col][row] = m[row][col]

		# Redefine `m` as a horizontal reflection of `m_t` (i.e. 90° clockwise from initial `m`)
		m = []
		for row in m_t:
			m.append(row[::-1])

		# Construct and return encrypted word
		encrypted = str()
		for row in m:
			for element in row:
				if element != '*':
					encrypted = encrypted + element
		return encrypted


# Input: `q` is a string of 100 or less of upper case, lower case, and digits
# Output: function returns a decrypted string
def decrypt(q):
	# Define length of string q
	length = len(q)

	# Exit if string is too long
	if length > 100:
		print('String is too long. Must be < 100 characters.')
		pass
	else:
		# Define smallest n x n matrix that can accommodate all values of q
		root = math.sqrt(length)
		n = math.ceil(root)

		# Add asterisks to string q, so that new length = n x n.
		asterisks_needed = (n * n) - length
		q_plus_asterisks = asterisks_needed * '*' + q
		q_temp_list = list(q_plus_asterisks)

		# Initialize empty n x n matrix `m`
		m = [[None for i in range(n)] for j in range(n)]

		# Fill in matrix `m` in row-major order
		for row in range(n):
			m[row] = q_temp_list[0:n]
			if row != n - 1:
				# Remove elements that have already been filled into `m`
				for element in range(n):
					q_temp_list.pop(0)

		# Remove input values, only want asterisks.
		for row in range(n):
			for col in range(n):
				if m[row][col] != '*':
					m[row][col] = None

		# Create matrix `m_t`, the transpose of `m`.
		m_t = [[None for i in range(n)] for j in range(n)]
		for row in range(n):
			for col in range(n):
				m_t[col][row] = m[row][col]

		# Redefine `m` as the vertical reflection of `m_t`
		m = m_t[::-1]

		# List of input string to be decrypted
		q_list = list(q)

		# From left to right, top to bottom, fill in empty elements with consecutive values of q_list
		for row in range(n):
			for col in range(n):
				if m[row][col] is None:
					m[row][col] = q_list[0]
					if len(q_list) > 1:
						q_list.pop(0)

		# Construct and return decrypted word
		decrypted = str()
		for col in range(n - 1, -1, -1):
			for row in range(n):
				if m[row][col] != '*':
					decrypted = decrypted + m[row][col]
		return decrypted


def main():
	# read the two strings P and Q from standard input
	p = input()
	q = input()

	# encrypt the string P
	p_encrypted = encrypt(p)

	# decrypt the string Q
	q_encrypted = decrypt(q)

	# print the encrypted string of P and the
	# decrypted string of Q to standard out
	print(p_encrypted)
	print(q_encrypted)


if __name__ == "__main__":
	main()
