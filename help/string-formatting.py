##
# @author Brandon Michael
# String formatting notes


# Basic Formatting
print("Basic Formatting")
print('%s %s' % ('one', 'two'))

print("Padding - Align right 10 spaces")
print('%10s' % ('test',))

print("Padding - Align left 10 spaces")
print('%-10s' % ('test',))

print("Truncating long strings")
print('%.5s' % ('xylophone',))

print("Truncating and padding")
print('%-10.5s' % ('xylophone',))

print("Padding numbers")
print('%4d' % (42,))
print('%06.2f' % (3.141592653589793,))
print('%04d' % (42,))

print("Length of a string")
print(len("Hello"))

print("Count character occurences")
print("Hello".count("l"))

print("Convert to uppercase and lowercase")
print("Hello".upper())
print("Hello".lower())

print("Finding strings")
print("Hello".startswith("Hello"))
print("Hello".endswith("asdfasdfasdf"))

print("Splitting string values")
print("Hello World".split(" "))
print("Hello,World".split(","))


print("col1 {0:20} col2 {1}".format("val1","val2"))

##
# Author: Brandon Michael
# The program displays states with their capitals in a two column format.

# Find the length of the city then add the correct number of tabs,
# then print the result
def printCapital(city, state):
  if len(city) > 8:
    print (city + "\t" + "\t"  + state)
  elif len(city) <= 8:
    print (city + "\t" + "\t" + "\t"  + state)
  
printCapital("Capital", "State")
printCapital("Topeka", "Kansas")
printCapital("Oklahoma City", "Oklahoma")
printCapital("Jefferson City", "Missouri")
printCapital("Des Moines", "Iowa")

##

print("%-10s%10.2f" % ("KANSAS", 6.52))