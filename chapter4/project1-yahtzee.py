##
# @author Brandon Michael
# This program simulates a simplified game of Yahtzee where a player
# plays against the computer.

# Allow your program to use the randint function
import random

# Create and initialize pre-loop "constants"
TWO_OF_KIND_POINTS = 25
YAHTZEE_POINTS = 50

# Create any other pre-loop variables you may need
userInput = "y"

# Running Total Values
userTotal = 0
computerTotal = 0

##
# Display the dice rolls based on the rules of Yahtzee with 3 rolls of a dice
def displaydicerolls(roll_1, roll_2, roll_3):
    if roll_1 == roll_2 and roll_1 == roll_3:
        return "Yahtzee! " + "(+" + str(YAHTZEE_POINTS) + ")"
    elif roll_1 == roll_2 or roll_1 == roll_3 or roll_2 == roll_3:
        return "Two of a Kind! " + "(+" + str(TWO_OF_KIND_POINTS) + ")"
    else:
        result = roll_1 + roll_2 + roll_3
        return "Chance! " + "(+" + str(result) + ")"

##
# Calculate and return the points awarded 3 rolls of a dice
# @return points awarded for the 3 rolls
def calculatedicerolls(roll_1, roll_2, roll_3):
    if roll_1 == roll_2 and roll_1 == roll_3:
        return YAHTZEE_POINTS
    elif roll_1 == roll_2 or roll_1 == roll_3 or roll_2 == roll_3:
        return TWO_OF_KIND_POINTS
    else:
        result = roll_1 + roll_2 + roll_3
        return result


# Continue to roll dice while the user enters an upper
# case or lower case Y.
while userInput == "y" or userInput == "Y":
    # For the player and computer, roll the three dice and display the dice
    # values. You will need to remember each die value.

    # Player Values
    userRoll1 = random.randint(1, 6)
    userRoll2 = random.randint(1, 6)
    userRoll3 = random.randint(1, 6)

    # Computer Values
    computerRoll1 = random.randint(1, 6)
    computerRoll2 = random.randint(1, 6)
    computerRoll3 = random.randint(1, 6)

    # If the values rolled were all the same, display "Yahtzee!"  and
    # and the number of points for a yahtzee are earned for the player
    # else if two values rolled were the same, display "Two of a Kind!" and
    # the number of points for two of a kind are earned for the player
    # else display chance and the sum of all three dice are earned for
    # the player and computer

    print("Player rolls: " +
          str(userRoll1) + ", " +
          str(userRoll2) + ", " +
          str(userRoll3) + "\n" +
          displaydicerolls(userRoll1, userRoll2, userRoll3))

    print("Computer rolls: " +
          str(computerRoll1) + ", " +
          str(computerRoll2) + ", " +
          str(computerRoll3) + "\n" +
          displaydicerolls(computerRoll1, computerRoll2, computerRoll3))

    # If you haven't already done so, tack the points earned onto
    # a running total for the player and computer

    userTotal = userTotal + calculatedicerolls(userRoll1, userRoll2, userRoll3)
    computerTotal = computerTotal + calculatedicerolls(
        computerRoll1, computerRoll2, computerRoll3)

    # Show the current totals
    print("=============================")
    print("Player total points: " + str(userTotal))
    print("Computer total points: " + str(computerTotal))
    print("=============================")

    # Prompt whether to roll again
    userInput = input("Roll again (Y or N)? ")
