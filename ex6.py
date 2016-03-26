x = "There are %d types of people." % 10 # this %d means you can input a raw value instead of going through a variable
binary = "binary" #making a string in a variable
do_not = "don't" #same as above
y = "Those who know %s and those who %s." % (binary, do_not) # you are putting in varaibles inside of a string. when more then 1, you use () separated by a comma

print x
print y

print "I said: %r." % x # the %r displays the raw data of the variable
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 