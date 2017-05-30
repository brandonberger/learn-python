ten_things = "Apples Oranges Crows Telephone Light Sugar" # string

print "Wait there are not 10 things in that list. Let's fix that." # string

stuff = ten_things.split(' ') # splits string into a list between spaces
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] # new list

while len(stuff) != 10: # while the amount of items in list is not 10
	next_one = more_stuff.pop() # removes and returns item in list if no index passes returns last
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
