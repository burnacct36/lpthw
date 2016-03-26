# Here are the instructions:

# 1. Open powershell and run python by typing python.
# Note: You have to be in the lpthw directory first
# Which looks like this: PS C:\Users\FG\lpthw
# Then you type python
# >>> python

# 2. Import the newly defined module (the script we created below). 
# >>> import ex25
# Note don't type .py b/c you'll get an error
# When you import this it will create a new file on your
# computer called "ex25.pyc", which is a "Python Bytecode
# Document", which helps the module load faster in the 
# future. You can, however, delete it if you want to.
 
# 3. Create an object(or variable) to work with.
# >>> sentence = "All good things come to those who wait."

# 4. Run "break_words" and show results
# >>> words = ex25.break_words(sentence)
# >>> words
# Note: you can also print without the intermediate variable:
# >>> print ex25.break_words(sentence)

# 5. Run "sort_words" and show results
# >>> sorted_words = ex25.sort_words(words)
# >>> sorted_words

# 6. Run "print_first_word" (displays automatically b/c we print in the function not return)
# >>> ex25.print_first_word(words)

# 7. Run "print_last_word" (displays automatically *** same reason as above)
# >>> ex25.print_last_word(words)

# 8. Run "sort_sentence" and show results
# >>> sorted_words = ex25.sort_sentence(sentence)
# >>> sorted_words

# 9. Run "print_first_and_last" (displays automatically)
# >>> ex25.print_first_and_last(sentence)

# 10. Run "print_first_and_last_sorted" (displays automatically)
# >>> ex25.print_first_and_last_sorted(sentence)

# If you type help(ex25) you'll see the block of
# text I wrote below the instructions and the text in
# triple quotes for each function below.

# If you type help(ex25.break_words) you'll see just
# the triple quote text for that function. That's called
# a "documentation comment."

# Finally, you can avoid typing "ex25." at the beginning
# of everything if you import the module like this instead:
# >>> from ex25 import *
# Note: make sure you are in the lpthw directory first
# Then you can run the commands like this:
# print break_words(sentence)

# And to quit Python:
# >>> quit()

# This is not a script. per se, but a module.
# That is, this document defines several functions
# that we can then use on other objects. The 
# module will be called "ex25" (without the .py
# extension). In addition, we are going to run 
# this from Python, and not the command line.

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ') # this built in function will let us split on spaces
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and the last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
# When should I print instead of return in a function?

# The return from a function gives the line of code that called the
# function a result. You can think of a function as taking input 
# through its arguments, and returning output through return. The
# print is completely unrelated to this, and only deals with
# printing output to terminal. 	