the_count = [1, 2, 3, 4, 5] # list of numbers
fruits    = ['apples', 'oranges', 'pears', 'apricots'] # list of strings
change    = [1, 'pennies', 2, 'dimes', 3, 'quarters'] # list of numbers & strings

# print each number in the_count list
for number in the_count: 
	print "This is count %d" % number

# print each string in the fruits list
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# print each value in change list
for i in change:
	print "I got %r" % i

# creates empty list
#elements = []
elements = range(0, 6)

# prints range of number 0 - 5 and adds to list
#for i in range(0, 6):
#	print "Adding %d to the list." % i
#	elements.append(i)

# prints each number in element list
for i in elements:
	print "Element was: %d" % i

