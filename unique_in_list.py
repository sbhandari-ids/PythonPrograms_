def find_it(seq):


    # for num in seq :
    #     if seq.count(num) %2 ==1:
    #     #print(seq.count(num))
    #         return num
            
            
            
    return {num for num in seq if seq.count(num)%2==1}

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))