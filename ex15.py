from sys import argv

script, filename = argv

txt = open(filename) #open is a command/function that reads our text file

print "Here's your file: %r " % filename
print txt.read() #this will print the text in our file in cmd line
#paranthesis are after functions because functions need arguments/additonal information.
#txt is the variable or the object
# the . is called the dot operator
# it is used to add a command, which in this case is read
# so line 8 is you take an object, txt, and the dot operator means do something on this object  

print "Type the filename again: "
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

#It's important to close files when you are done with them.
txt.close
txt_again.close

#we closed both of our objects/variables.