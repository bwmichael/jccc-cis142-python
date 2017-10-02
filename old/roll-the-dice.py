##
# @author Brandon Michael
# Roll the dice based on the user's input. Track double rolls and display
# the double totals.

# import the random library
import random

# Set the start and end values the same as a dice
start = 1
end = 6

# Set the running total for doubles found
totalDoubles = 0

# Get the number of times we need to roll the dice
rolls = int(input("Enter the number of dice rolls: "))

# Loop through the number of rolls
for num in range(0, rolls, 1):
    # Capture the rolls to check for doubles
    roll_1 = random.randint(start, end)
    roll_2 = random.randint(start, end)

    # Check if rolls equal each other, and track the double count
    if roll_1 == roll_2:
        totalDoubles = totalDoubles + 1
        print(roll_1, roll_2, "Double !")
    else:
        print(roll_1, roll_2)

# Print the results
print(totalDoubles, "double(s) rolled.")
