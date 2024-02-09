def unique_in_order(seq):
    
    list_unique = []
    list_seq = seq
    print(seq)
    if len(list_seq)==0:
        return []
    if len(list_seq)==1:
        return list(list_seq)
    for index, letter in enumerate(seq):
        if letter[index] == letter[index+1]:
            print(letter[index], letter[index+1])
            if letter in list_unique:
                continue
            else:
                list_unique.append(letter)
        else:
            list_unique.append(letter)
            
        print(list_unique)

print(unique_in_order(['aa']))