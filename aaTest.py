def duplicate_encode(word):
    #your code here
    
   # word1 = word.split()
    
    word1 = ([*word])
    letters = []
    duplicates = []
    word2 = ""

    for letter in word1 : 
        if letter in letters:
            duplicates.append(letter)
        else: 
            letters.append(letter)

    print(letters)
    print(duplicates)

    final_word = ""

    for letter in word1:
        if letter in duplicates :
            final_word += "".join(')')
        else : final_word += "".join('(')
            
    return final_word

        
        
            



    return word1




print(duplicate_encode("recede")) 