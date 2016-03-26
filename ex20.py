from sys import argv

script, input_file = argv

def print_all(f):  # this function displays an entire text file
	print f.read() # 'f' is just a variable name for the file.
	
def rewind(f):
	f.seek(0) # each time you do seek(0) you're moving to the start of the file
	
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file) # you have to open the file so python can read it

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
