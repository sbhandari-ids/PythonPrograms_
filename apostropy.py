str =  "  'My name is same as my Dad's name.'  "
str1 = "Hello"
str2 = "'what is your cat's name'" 
str3 = "Albert Einstein once said, “A person who never made a mistake never tried anything new.”"
print(str.lstrip()+str1) # removes the white space on the left of the string
print(str.rstrip()+str1) # removes the white space on the right of the string
print(str.strip()+str1) # removes the white space on the both left and right of the string
print(str+str1) # prints the concatenated string combining str1 and str2
print(str2) # remove the double quotes (" ") and try running this application to test the apostrophy error. 
print("*"*30)
print(str1.upper())
print(str1.lower())
print(str1.title())
print("*"*30)
print("\tAlbert Einstein once said, “A person who never made a \n\tmistake never tried anything new.”")
