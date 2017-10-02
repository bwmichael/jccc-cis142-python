##
# @author Brandon Michael
# Get the starting integer, ending integer, and the step size. Check if the user
# entered correct values, then display the results

# Get user input
startInt = int(input("Starting integer: "))
endInt = int(input("Ending integer: "))
stepSize = int(input("Step size: "))

# Setup variables for tracking the iteration results
runningTotal = startInt
result = ""

# Use a for loop to iterate through the range
for num in range(startInt, endInt, stepSize):
    result = result + str(runningTotal) + " "
    runningTotal = runningTotal + stepSize

# Check if range was valid, then print the result
if result == "":
    print("Invalid step size.")
else:
    print(result)
