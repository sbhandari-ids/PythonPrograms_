def vowels_in_sentence(sentence):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    #sentence = 'this is my sample sentence'    
    for index in range(len(sentence)):
     if sentence[index].lower() in vowels:
        vowel_count+=1
    return vowel_count     

vowelcount = print(vowels_in_sentence("Row Eow Row the Boat Gently down the steam"))