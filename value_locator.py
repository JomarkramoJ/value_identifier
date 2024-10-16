#Define 5 variables
def find_highest(first, second, third, fourth, fifth):
    highest = first

#Compare all variables
    if second > highest:
        highest = second

    if third > highest:
        highest = third
    
    if fourth > highest:
        highest = fourth

    if fifth > highest:
        highest = fifth

    print("The highest number is: ", highest)

#Ask for user to input 5 variables
while True:
    try:
        first = int(input("Enter the first number: "))
        break
    except ValueError:
        print("Please enter a valid number: ")
        
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
fourth = int(input("Enter the fourth number: "))
fifth = int(input("Enter the fifth number: "))

#Print highest number

