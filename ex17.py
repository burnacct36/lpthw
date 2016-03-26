# We're writing a script to copy one file to another

from sys import argv
from os.path import exists

# os.path is used because different operating
# systems (e.g. mac, windows, linux) specify
# files paths in diferent ways. 'exists' is a 
# function that returns "TRUE" if the file path
# is valid.

script, from_file, to_file = argv

# need to give name of files that you are copying
# from and copying to in the command line when
# you run this python script

print "Copying from %s to %s." % (from_file, to_file)

# we could do the following two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# ANS: one line --> indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("?")

out_file = open(to_file, 'w')
out_file.write(indata) # we write the data to the out_file

print "Alright, all done."

out_file.close()
in_file.close()

