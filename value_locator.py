#Define 5 variables
#Compare variables 1 to 2
#If variable 1 greater than 2
    #Compare variable 1 to 3
    #If variable 1 greater than 3
    #Return to Variable 1, else return to variable 3
#Repeat process until all 5 variables have been compared
#Ask for user input and find highest variable
def find_highest(first, second, third, fourth, fifth):
    highest = first

    if second > highest:
        highest = second

    if third > highest:
        highest = third
    
    if fourth > highest:
        highest = fourth

    if fifth > highest:
        highest = fifth

print("The highest number is: ", highest)


