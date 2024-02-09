for num in range(1,100):
    cube = num * num * num 
    print(cube)
    if cube>=1000:
        break

# List Comprehension Method 

cube = [num*num*num for num in range(20) if num*num*num <=1000]
print(cube)