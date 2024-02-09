sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def sheep_count(sheeps):
    count = 0
    for sheep in sheeps :
        if sheep == True:
            count+=1
    return count

    list(lambda count: count+=1 for sheep in sheeps if sheep:)

