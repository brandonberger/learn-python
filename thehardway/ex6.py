x = "There are %d types of people." % 10 # sets variable x to a string with a number inside
binary = "binary" # sets variable binary to string
do_not = "don't" # set variable do_not to string
y = "Those who know %s and those who %s." % (binary, do_not) # sets variable y to a string with two variables inside that were asigned above

print x # prints variable x
print y # prints variable y

print "I said: %r." % x # prints string with a formatted variable inside that equals variable x
print "I also said: '%s'." % y # prints string with formated variable inside that equals variable y

hilarious = False # sets variable hilarious to false
joke_evaluation = "Isn't that joke so funny?! %r" # sets variable to string with formatted string inside

print joke_evaluation % hilarious # prints joke variable and sets the formatted variable inside to variable hilarious

w = "This is the left side of..." # sets variable to string
e = "a string with a right side." # sets variable to string

print w + e # prints & concatenates variable strings w & e

##### Notes ######

# %r is used for debugging, while %s is used for displaying to users
