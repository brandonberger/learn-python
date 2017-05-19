def print_two(*args): # defines function and asigns passed parameters to args as a list aka array
	arg1, arg2 = args # asigns indiviual variables to the passed arguments
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2): # defines function and asigns each parameter to its own variable
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" %arg1

def print_none():
	print "I got nothin'."

# calls functions
print_two("Bdon", "bergers")
print_two_again("bdon", "bergers")
print_one("First!")
print_none()


######################################################
##################Practice############################
######################################################


def person(first_name, last_name):
	print "Name: %s %s" % (first_name, last_name)

def setName():
	name = []
	name.append("Brandon")
	name.append("Berger")
	return name

def getName():
	name = setName()
	person(name[0], name[1])


getName()