# Exercise 10: What Was That?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# ADDENDUM

print "\\\\ = \\ \n"
print "\\\' = \' \n"
print "\\\" = \" \n"
print "bla\\abla = bla\abla \n"
print "bla\\bbla = bla\bbla \n"
print "bla\\fbla = bla\fbla \n"
print "bla\\nbla = bla\nbla \n"
print "bla\\N{name}bla = bla\N{name}bla \n"
print "bla\\rbla = bla\rbla \n"
print "bla\\tbla = bla\tbla \n"
print "\\u0ABC = \u0ABC \n"
print "\\U0ABC1111 = \U0ABC1111 \n"
print "bla\\vbla = bla\vbla \n"
print "\\777 = \777 \n"
print "\\x21 = \x21 \n"

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,
