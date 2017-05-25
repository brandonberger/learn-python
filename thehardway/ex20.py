from sys import argv # is a list which contains the command-line arguments passed to the script

script, input_file = argv #asigns variables to list items

def print_all(f): #defines function with 1 parameter
	print f.read() # print the output of the function read() on the parameter passed through

def rewind(f): # defines function with 1 parameter
	f.seek(0) # ? 

def print_a_line(line_count, f): # defines function with two parameters
	print line_count, f.readline() # prints param1 and the output of the function readline() on param2

current_file = open(input_file) # asigns var to return value of the function open with the txt file passed in it

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)