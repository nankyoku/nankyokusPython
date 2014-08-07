# Exercise 3: Numbers and Math

# + plus (addition in so many ways)
# - minus (question to self, does this mean substraction in so many ways too?)
# / slash (also division)
# * asterisk (also multiplication, is ** a power too?)
# % percent (also modulus)
# < lesser-than
# > greater-than
# <= lesser-than-or-equal-to
# >= greater-than-or-equal-to

# This line only prints the phrase "I will now count my chickens:"
print "I will now count my chickens:"

# This line prints "Hens" and whatever Python computes for 25 + 30 / 6, which should be 30 in fact. 
print "Hens", 25 + 30 / 6

# This line prints "Roosters" and whatever Python computes for 100 - 25 * 3 % 4 (here I am not sure about the order, weather it does the * or % first. 
# In fact I just checked, it does first 25 * 3, and then computes the remainder of 74 / 4, which is 75 % 4 = 3. 
print "Roosters", 100 - 25 * 3 % 4

# This line prints "Now I will count my eggs:"
print "Now I will count my eggs:"

# This line prints the result from the following computation: 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 (which should be 6.75, but as we are not dealing with floats, then it should be 7 if I did my math right). 
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# This line prints: "Is it true that 3 + 2 < 5 - 7?"
print "Is it true that 3 + 2 < 5 - 7?"

# This line prints the truth value of 3 + 2 < 5 - 7
print 3 + 2 < 5 - 7

# This line prints "What is 3 + 2?" and the computation fo 3 + 2 which is 5. 
print "What is 3 + 2?", 3 + 2

# This line prints "What is 5 - 7?", and the computation f 5 - 7 which is -2. 
print "What is 5 - 7?", 5 - 7

# This line prints "Oh, that's why it's False."
print "Oh, that's why it's False."

# This line prints "Is it greater?" and then the truth value of 5 > - 2 (True). 
print "Is it greater?", 5 > -2

# This line prints "Is it greater or equal?" and then the truth value of 5 >= -2 (which is still True). 
print "Is it greater or equal?", 5 >= -2

# This line prints "Is it lesser?" and then the truth value of 5 < -2 (False). 
print "Is it less or equal?", 5 <= -2

print "\nAddendum: Using floats"
print "Now I will recount my eggs:"
print 3.0 + 2.0 + 1.0 - 5.0 + 4 % 2 - 1.0/4.0 + 6.0
