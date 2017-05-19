## Using else with a loop
## executed when the loop terminates trhough exhaustion of the list with (for)
## or when the condition becomes false with (while)
## does not execute when break is used
#i.e

for n in range(2, 10):
	for x in range(2, n):
		if (n % x == 0):
			print n, 'equals', x, '*', n/x
			break
	else:
		print n, 'is a prime number'


## the continue statement
#i.e

for num in range(2, 10):
	if num % 2 == 0:
		print "Found an even number", num
		continue
	print "Found a number", num