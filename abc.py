# Grasshopper - Summation
# DESCRIPTION:
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# For example (Input -> Output):
# summation(2) -> 3 (1 + 2)
# summation(8) -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

# define a function with a parameter num. 
# loop it thru using range
# and add each number until it reaches num. 

def grasshopper_sum(num):
    total = 0
    for item in range(num+1):
        total += item

    return total

print(grasshopper_sum(8))


def mySum(myList):
    return sum(range(myList + 1))
print(mySum(8))