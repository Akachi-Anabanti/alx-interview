#!/usr/bin/python3
'''Pascal Triangle'''

def pascal_triangle(n):
	"""Defines a function that
	generates the pascal triangle of order
	'n'"""
	if  n == 0:
		return []
	elif n == 1:
		return [[1]]
	else:
		triangle = pascal_triangle(n-1)
		last_row = triangle[-1]
		new_row = [1]
		for i in range(len(last_row) - 1):
			new_row.append(last_row[i] + last_row[i + 1])
		new_row.append(1)
		triangle.append(new_row)
		return triangle


n = 6
triangle = pascal_triangle(n)
for i in triangle:
	print(i)
