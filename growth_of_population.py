
def nb_year(p0, percent, aug, p):
    # your code
    index = 0
    pn = 0
    while(pn<p):
        
        pn = p0 + p0*percent/100 + aug
        
        p0 = int(pn)
        
        index +=1 
        
    return index


print(nb_year(1500, 5, 100, 5000))#, 15))
print(nb_year(1500000, 2.5, 10000, 2000000))#, 10)
print(nb_year(1500000, 0.25, 1000, 2000000))#, 94)
        