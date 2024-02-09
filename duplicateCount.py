def duplicate_count(text):
    # # Your code goes here
    #  text=str(text).lower()
    #  #text.toList()
    #  print(text[0])
    #  text_list = text.split()
    #  print(text_list)
    #  print(text[0])
    #  duplicates = 0; 
    #  for chars in text:
    #         for letter in range(1,len(text)):
    #               print(chars)
    #               print(letter)
    #             # if chars == letter : 
    #             #     duplicates +=1 
     
    #  index=1  
    #  duplicate_count =0        
    # #  return duplicates
    #  for letter in text:    
    #     print(letter)
    #     print(text[index])
        
    #     if letter == text[index]:
    #         duplicate_count+=1
    #         print("dupli_count : ", duplicate_count)
    #     else: print("no match ", index)

    #     if index < len(text)-2:
    #         index+=1

    #  print(duplicate_count)
    #  return duplicate_count



    #         if letter == text[index]:
    #             duplicate_count+=1
    #         else: print("no match ", index)

    #         index+=1 
     duplicate_count =0
     uplimit = len(text)-1
     x=0 
     y=1
     dupli_place=[]
     test_char=[]
     for numi in range(x,uplimit):
        for numj in range(y,uplimit+1):
            if(str(numi) in test_char):
                print("pass")
            else:
                print (text[numi])
                print (text[numj])
                if text[numi]==text[numj]:
                    dupli_place=str(numi+1)+str(numj+1)
                    duplicate_count +=1
                    print("............Y ",dupli_place)
                
            test_char = str(numi)
        y+=1
        
     x+=1

     
            
     
     return duplicate_count

dupliCount = print(duplicate_count("rrrraaram"))

