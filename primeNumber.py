# num = int(input("Enter a whole number"))

# print("welcome to prime number test")

# num = 1

# while(num <=100):
#     compNum=False
#     for number in range(2, (int(num/2) +1)):
#         if number!= num:
#             if num % number == 0: 
#                 compNum = True
        
#     if compNum==False:
#         print("prime number : ",num)
#     num+=1

print("welcome to prime number test")

number = 1

while(number <=100):
    prime = True
    for div in range(2, (int(number/2) +1)):
        if div!= number:
            if number % div == 0: 
                prime = False
        
    if prime==True:
        print("prime number : ",number)
    number+=1