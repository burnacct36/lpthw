#raw_input() gives the user of your program to fill in information

print "How old are you?", #we put a comma at the end of each print line.
age = raw_input()
print "How tall are you?", #this is so print doesn't end the line with a newline
height = raw_input()
print "How much do you weigh?", #character and go to the next line.
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (
	age, height, weight)
