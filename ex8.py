# Exercise 8: Printing, Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.", 
	"That you could type up right.", 
	"But it didn't sing.",
	"So I said goodnight."
)


# Python recognizes True and False as keywords representing the truth-values. IF you put quotes around them then they are turned into strings and they won't work as truth values.
