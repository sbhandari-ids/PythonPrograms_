def words_to_marks(s):
    list_of_letters = [*s]
    list_of_numbers = []
    #return list_of_letters
    for letter in list_of_letters:
        letter = ord(letter)-96
        list_of_numbers.append(letter)
    print(list_of_letters)
    print(list_of_numbers)
    return sum(list_of_numbers)
    
    #return sum(list_of_letters)
    
    
print(words_to_marks("attitudeisattitude"))