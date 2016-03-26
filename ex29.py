# An if-statement creates what is called
# a "branch" in the code. The if-statement
# tells your script, "If this boolean expression
# is True, then run the code under it, otherwise skip it." 

people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"


dogs += 5 

# What does += mean?
# The code x += 1 is the same as doing x = x + 1 but
# involves less typing.

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	

if people == dogs:
	print "People are dogs."
	
	