#! /usr/bin/env python3
# Practice task to make a table
# out of lists of strings

tableData = [['Company', 'CEO', 'Product'],
			 ['Google', 'Lary', 'Search Engine'],
			 ['Facebook', 'Mark', 'Social Network'],
			 ['Tesla', 'Elon', 'Car Manufacturer'],
			 ['Apple', 'Tim', 'Electronics'],
			 ['Amazon', 'Jeff', 'Online Shopping'],
			 ['Twitter', 'Jack', 'Social Network'],
			 ['Microsoft', 'Bill', 'PCs & Software'],
			 ['Uber', 'Unkown', 'Mobile App']]

def printTable(title, data):
	table = title.center(10, '-') + '\n'
	colWidth = 0
	for k in data:
		if colWidth > 0:
			if colWidth < len(k[0]):
				colWidth = len(k[0])
				print(k[0])
		else:
			colWidth = len(k[0])

		table = table + k[0].ljust(colWidth, ' ') + k[1].ljust(colWidth, ' ') + k[2].ljust(colWidth, ' ') + '\n'
		# colWidth = 0
	# print(table)

printTable('Tech Companies', tableData)
