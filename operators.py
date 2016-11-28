## Basic Operators in Python

## Arithmetic Operators
## Order of operations
# i.e 
number = 1 + 2 * 3 / 4.0 # returns 2.5

## The modulo operator, which returns the remainder of the division
# i.e
remainder = 11 % 3 # retuns 2

## Power relationship operators 
## Two multiplication symbols (*)
# i.e
squared = 7 ** 2 # retuns 49
cubed = 2 ** 3 # returns 8


## Operators on Strings (concatenation)
# i.e
helloworld = "Hello" + " " + "World" # returns Hello World

## Multiplying Strings
#i.e
lostsofhellos = "hello" * 10 # returns hellohellohellohellohellohellohellohellohellohello

## Using operators with lists
## Lists can be joined using addition operators
#i.e
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers # returns [1, 3, 5, 7, 2, 4, 6, 8]

## Multiplying Lists
#i.e
sequences = [1,2,3] * 3 # returns [1, 2, 3, 1, 2, 3, 1, 2, 3]

## Exercise
x = object()
y = object()

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print "x_lists contains %d objects" % len(x_list)
print "y_list contains %d objects" % len(y_list)
print "big_list contains %d objects" % len(big_list)

if x_list.count(x) == 10 and y_list.count(y) == 10:
	print "Almost there..."
if big_list.count(x) == 10 and big_list.count(y) == 10:
	print "Great!"