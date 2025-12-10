# Write a Python program to get the smallest number from a list
import sys
data = list(range(1, 11))
smallest = sys.maxint
for x in data:
    if x < smallest:
        smallest = x

print(smallest)