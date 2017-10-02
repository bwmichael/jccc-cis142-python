# Brandon Michael
# CIS 142
# Get length and width input values, run some basic calculations, then display results


## import Math libraries
import math


## Declare functions

## Calculate the Perimeter of a rectangle
## P = (2l) + (2w)
def calcPerimeter(l, w):
  length = int(l)
  width = int(w)
  result = (2*length) + (2*width)
  return result

## Calculate the Area of a Rectangle
## A = wl
def calcArea(l, w):
    length = int(l)
    width = int(w)
    result = width*length
    return result

## Calculate the Diagnol in a rectangle
## a^2 + b^2 = c^2
def calcLength(l, w):
    length = int(l)
    width = int(w)
    # Using the round function to go to 3 decimal places
    result = round(math.sqrt((width**2) + (length**2)),3)
    return result


# Get the input values
inputLength = input("Length in feet: ")
inputWidth = input("Width in feet: ")

print("Perimeter:" , calcPerimeter(inputLength, inputWidth),  "feet")
print("Area:",  calcArea(inputLength, inputWidth), "sq ft")
print("Diagonal:" , calcLength(inputLength, inputWidth) , "feet")