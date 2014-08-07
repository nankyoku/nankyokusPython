# Exercise 4: More Variables and Printing

# -- coding:utf-8 --


my_name = "Nan Kyoku"
my_age = 36 # was tempted to lie
my_height = 1.76 # meters
my_weight = 228 # lbs
my_weight_goal = my_weight - 176
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'


print "Let's talk about %s." % my_name
print "She's %f meters tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Her goal is to loose %d pounds." % my_weight_goal
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s unless she ate something weird." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %f, and %d I get %f." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# Study drills

# 1. The study drills call to change all the variable names so there isn't a "my_" in front, but I won't do that, I like that their "mine". 

# 2. Try to write some variables that convert the inches and pounds to centimeters and kilos. Do not just type in the measurements. Work out the math in Python. 

# Computes height in inches (first convert meters to centimeters -1 meter = 100 cm., then convert centimeters to inches, 1 inch = 2.54 cm). 
my_height_in = 100*my_height/2.54 # inches

# Computes the weight in kilograms (1 pound = 0.453592 kgs).
my_weight_kg = my_weight*0.453592

print "The height in inches is %r, and the weight in kilograms is %r." % (my_height_in, my_weight_kg)

# 3. Rain check on searching online for all of the Python format characters. 

# 4. When using %r as a format character, it says "print this no matter what.". 

