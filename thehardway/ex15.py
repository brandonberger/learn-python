from sys import argv # imports module

script, filename = argv # sets variables to passed arguments

txt = open(filename) # sets var to contents of file 

print "Here's your file %r:" % filename 
print txt.read() # prints the contents of the file

done = raw_input("Are you done? Y/N")
if done == 'y':
	txt.close()
	print 'File closed'
else:
	print "hurry up"
