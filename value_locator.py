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



