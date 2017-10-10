##
# @author Brandon Michael
# This program asks the user for a year that we can check to see if it is a 
# leap year or not.

## Determines if a year is a leap year
# @param year The year to test (Integer)
# @return true or false where the year is a leap year
def isLeapYear(year):
    
    # If the year is divisible by 400 or 100 and divisible by 4 then its
    # a leap year.
    if (year%400==0 or year%100!=0) and (year%4==0):
        return True
    else:
        return False

## Displays the welcome message to the program
# @return string message describing the program
def welcomeMessage():
    return "Enter a year to validate if it is a leap year!"

## This is the main entry point to the program
def main():
    
    # Set the input to y for the first checking of the leap year
    userInput = "y"
    
    # Always loop until a break occurs
    while True:
        
        # Check if the user wants to continue
        if userInput == "y" or userInput == "Y":
            
            # Get the year and convert it to an integer
            inputYear = int(input("Please enter a year to test: "))
            
            # Check to make sure the user entered a valid year
            if inputYear >= 0:
                
                # Check to see if the leap year function is returning true
                # or false. Print the result with the year.
                if isLeapYear(inputYear):
                    print(str(inputYear) + " is a leap year!")
                else:
                    print(str(inputYear) + " is not a leap year.")
                
                # Ask the user if they want to continue
                userInput = input("Enter another leap year? (y or n): ")
            else:
                
                # Set the userInput to yes so we can check the year instead of
                # prompting the user
                userInput = "y"
            
        # Check to see if the user wants to continue
        elif userInput == "n" or userInput == "N":
            
            # Exit the loop and exit the program.
            break

# Describe to the user what the program does
print(welcomeMessage())

# Call the main function to start up the program
main()