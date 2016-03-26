#List of functions/commands/methods to memorize.

#close - closes the file.
#read - reads the contents of the file.
#readline - reads just one line of a text file.
#truncate - empties the file. Watch out if you care about the file.
#write("stuff") - writes "stuff" to the file.
#write takes a parameter of a string you want to write to the file.

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') # if you use 'w' then you're saying open this file in 'write' mode.

#w = write (vs. r for for read and a for append)
#r is read only is the default of the open() functions/commands/method
#w+ lets you read and write. it opens the file for writing(truncates it to 0 bytes)
#but also lets you read from it.
#if you use r+ it is also used for both reading and writing, but won't be truncated. 

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n") #these make sure you get a new line
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#target = open(filename) #had to do it this way because w+ in line 21 was running funky.
#print target.read()

print "And finally, we close it."
target.close()


