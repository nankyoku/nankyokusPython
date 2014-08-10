# Exercise 6: Strings and Text

# The below 4 statements set up variables and their values
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# The below 2 statements print out the values of the variables x and y. 
print x
print y

# The statement below prints a string and variable x, note that we're using type %r.
print "I said: %r." % x

# The statement below prints a string and variable y, note that we're using type %s, and it is in between ' ' which seems to make no difference for the string that was defined with " ". 
print "I also said: '%s'." % y

# Setting up variables as well in the following 2 statements. 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# printing two variables, this is interesting because the first variable is a string, and it is using %r. It seems there are subtleties as how to use these. Will keep on studying. 
print joke_evaluation % hilarious

# Setting up two variables and their values. 
w = "This is the left side of..."
e = "a string with a right side."

# Printing the two variables above, which were strings. 
print w + e

