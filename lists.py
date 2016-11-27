## Lists are very similar to arrays
## They can contain any type of variables
## They can also have as many variables as you wish

## Initiating a list i.e
mylist = []

## adding to a list
mylist.append(1)
mylist.append(2)
mylist.append(3)

## printing list items
print(mylist[0])
print(mylist[1])
print(mylist[2])

## loops through a list
for x in mylist:
	print x


## Exercise
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings = []
strings.append("Hello")
strings.append("World")

names = ["Remy", "Joe", "Zen"]

second_name = names[1]

print(numbers)
print(strings)
print("The scond name on the names list is %s" % second_name)