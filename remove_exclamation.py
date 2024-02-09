def remove(st, n):
    new_string = ""
    if n>len(st):
        loop_count = len(st)
    else: loop_count = n
    i=0
    count = 0
    for number in range(loop_count):
        if st[i] == "!" and count >= n: 
                new_string+= st[i]
                count+=1
        else: new_string+= st[i]
        
        i+=1       
                
    return new_string

new_str = print(remove("Hi!!!", 2))