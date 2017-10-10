def isLeapYear(year):
    if (year%400==0 or year%100!=0) and (year%4==0):
        return year + "is a leap year!"
    else:
        return year + "is not a leap year!"

def main():
    
    userInput = "y"
    while userInput == "y" or userInput == "Y":
        inputYear = int(input("Please enter a year to test: "))
        print(isLeapYear(inputYear))
        
        # Prompt 
        userInput = input("Enter another leap year? (y or n): ")
    
main()