#to create a function that will add up all the numbers in a list of numbers
#list of numbers are given as an argument
#use the function to ask the user for series of numbers
#and, show the user the sum of numbers given by users.

from os import system, name # used in screen clear function
import time                 # used in time.sleep() function

def number_adder(myList):
    sum = 0
    for num in myList:
        sum+=num
   # print(sum)
    return sum; 


# define our screen clear function 
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear') # Then, whenever you want to clear the screen, just use this clear function as: clear()


print("Hello there !")
num_list = []
num = input("add a new number to the numbered list or type 'q' to quit ")
    
while (num != 'q' ):
   # print (index)
    num_list.append(int(num))
    num = input("add a new number to the numbered list or type 'q' to quit ")
        


print("The sum of number list is : ", number_adder(num_list))
print("About to clear the screen.....")
time.sleep(7) # delays the execution of next step by number of seconds in the parameter. import time. 
clear()