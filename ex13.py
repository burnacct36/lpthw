#the ex13.py from python ex13.py is called an argument.

#So what is a script?
#Script: basically a text file containing the statements that
#comprise a Python program.

#the following is a script that accepts arguments.

#sys is a feature that we import. we call it a module or library.
from sys import argv 

#argv is a argument variable. it holds the arguments you pass
# from cmd line to your python script.

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third 