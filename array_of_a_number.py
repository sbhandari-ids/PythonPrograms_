# Convert number to reversed array of digits

# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):

# 35231 => [1,3,2,5,3]
# 0 => [0]

def num_to_reversed_array(number):
    
    reversed_array=[]
    for digit in str(number) : 
        item = int(number)%10
        number = int(int(number)/10)
        #reversed_array+=str(item)
        reversed_array.append(item)
        print(item)
        print(number)        #reversed_array+=item

    return reversed_array

rev_array = print(num_to_reversed_array(93326465793638890))


    