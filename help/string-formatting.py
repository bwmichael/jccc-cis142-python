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
print('%.2f' % (3.141592653589793,))
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

print("Repetition")
print("123"*3)

print("Positioning")
print("Hello"[1])

print("Finding Length")
print(len("Hello"))

print("Replacing string values")
print("Hello".replace("ello", "ELLO"))

print("Changing case")
print("name".upper())
print("name".lower())

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


## OUTPUT

# Basic Formatting
# one two
# Padding - Align right 10 spaces
#       test
# Padding - Align left 10 spaces
# test      
# Truncating long strings
# xylop
# Truncating and padding
# xylop     
# Padding numbers
#   42
# 003.14
# 0042
# Length of a string
# 5
# Count character occurences
# 2
# Convert to uppercase and lowercase
# HELLO
# hello
# Finding strings
# True
# False
# Splitting string values
# ['Hello', 'World']
# ['Hello', 'World']
# col1 val1                 col2 val2
# Capital                 State
# Topeka                  Kansas
# Oklahoma City           Oklahoma
# Jefferson City          Missouri
# Des Moines              Iowa
# KANSAS          6.52