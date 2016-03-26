# What does 'return' do?
# 'return' creates a value that can be
# assigned to a variable that calls the function.

def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

# Don't forget you can have float(raw_input())
# as an argument or int(raw_input()) too.


age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# By calling the functions to assign values to variables.
# two things happen: (1) the function runs, which is why
# their text appears in the console; and (2) the resulting
# value is assigned to the variable; which is why it can 
# fill in the next string.

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
