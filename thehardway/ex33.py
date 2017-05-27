numbers = []


def makeList(start = False, end = False):
	while start < end:
		numbers.append(start)
		start = start + 1


#while i < 6:
#	print "At the top i is %d" % i
#	numbers.append(i)

#	i = i + 1
#	print "Numbers now: ", numbers
#	print "At the bottom i is %d" % i

print "The numbers: "
makeList(3, 8)
for num in numbers:
	print num
