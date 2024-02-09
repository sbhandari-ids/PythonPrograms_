def duplicate_count(text):
    # Your code goes here
     
    text = [*text]
    print(text)
    duplicates =[]
    origin = []
    for letter in text:
        if letter in origin:
            duplicates.append(letter)
        else : origin.append(letter)
    print(origin)
    print(duplicates)
    return len(duplicates)
        
print(duplicate_count("aabbcddee"))