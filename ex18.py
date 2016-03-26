# this one is like your scripts with argv
def print_two(*args): # we ended this function with a semi-colon
	arg1, arg2 = args # make sure to indent(four spaces)   
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this takes no arguments
def print_none():
	print "I got nothin'."

# NB: a function with no arguments still does
# something. It just doesn't need any variables
# added to do its job.	

print_two("Filip","Gasior")
print_two_again("Filip","Gasior")
print_one("First!")
print_none()