from sys import argv # imports from the Python feature set, edit: not called features they are called modules!
	# argv is the argument variable, it holds the arguments you pass to the file on run
script, first, second, third = argv  # unpacks argv and asigns variables to the contents

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

				   
# ran by: ` python ex13.py first 2nd 3rd ` 
					