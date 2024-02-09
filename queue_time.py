def queue_time(customers, n):
    pass # TODO

    new_list = []
    time_sum = index = 0
    if not customers : return 0
    
    if n == 1 : return sum(customers)
    
    if n>=2:
        if len(customers) <= n :
            return max(customers)
        else : 
            for customer in customers:
                while(index<len(customers)):
                    time_sum += customers[index]
                    index += n

                    print("Printing Customer @ Index ", customers[index], index)
                    # time_sum += customers[index]
                    print("Printing Sum @ Index" , time_sum, index)
                    # index += n
                
                new_list.append(time_sum)
                
        print(new_list)    
                
        return max(new_list)
    
queue_time([14, 11, 43, 10, 23, 7, 42, 8, 27, 6, 1, 31, 26, 8, 24, 11], 4 )