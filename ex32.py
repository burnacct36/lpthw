# Before you can use a for loop, you need a way to store the results of loops
# somewhere. The best way to do this is with lists. Lists are exactly what 
# their name says: a container of things that are organized in order from first
# to last. It's not that complicated; you just have to learn a new syntax. First,
# there's how you make lists:

# hair = ['brown', 'blond', 'red']
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]

# In python these collections of data are called "lists."
# In many other languages they are called "arrays."

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	# the first variable (right after "for") can use
	# any name you like. although i is common
	print "This is count %d" % number # %d b/c the numbers are values
	
# same as above
for fruit in fruits:
	# don't use the same name twice
	print "A fruit of type: %s" % fruit # %s b/c the fruits are strings

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	# 'i' is the most common variable name for-loops
	print "I got %r" % i # %r b/c the list contains different types
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	# Range starts at the first number (inclusive) but
	# stops at 1 less than second number (exclusive)
	# But 0 as first number is default, so this can
	# also be written as "range(6)"
	# Can also specify whether range goes up or down
	# and size of steps.
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
	# This adds the numbers to the list one at a time
	
# now we can print them out too
for i in elements:
	print "Element was: %d" % i

# and here is an easier way to fill in the list in one command
# elements2 = range(6)
# for i in elements2:
#	 print "elements2 item was: " % i 

















