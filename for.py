## Basic for statement in python
## The for loop in python can iterate over strings & lists
#i.e

words = ['cat', 'window', 'defenstrate']
for w in words:
	print w, len(w)


## modifying while inside the loop
#i.e

for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

print words