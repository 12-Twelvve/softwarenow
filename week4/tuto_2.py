# Define a function named sum. This function expects two numbers, named low and high, as
# arguments. The function computes and returns the sum of all of the numbers between low
# and high, inclusive.

def sum(low, high):
    sum = 0
    for x in range(low, high+1):
        sum +=x
    return sum

        

