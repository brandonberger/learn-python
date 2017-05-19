from sys import argv
from os.path import exists # returns True if a file exists, based on its name in a string as an argument. 

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file) # opens file with the to be copied text 
indata  = in_file.read() # reads the contents of to be copied txt file

print "The input file is %d bytes long" % len(indata), # len() gets the length by byte of the to be copied file
print "Does the output file exist? %r" % exists(to_file), # checks if file exists
print "Ready, hit RETURN to continue. CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w') # opens file to paste in
out_file.write(indata) # writes to file the contents of copied file
print "Alright, all done."

out_file.close()
in_file.close()