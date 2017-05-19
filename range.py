## If you do need to iterate over a sequence of numbers, the range function works
#i.e

print range(10)

## by default the range will start at the int 0
## to change the start & stop 
#i.e

print range(5, 10)

## Range can even do different increments 
#i.e

print range(0, 10, 3)

## len() i.e

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print i, a[i]
