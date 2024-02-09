import string
def alphabet_position(text):
    index = 1
    alpha_dict = {}
    for letter in string.ascii_lowercase:
        alpha_dict[letter] = index
        index+=1
    print(alpha_dict)

    letter_list = [char for char in text.lower() if char.isalpha()]
    print(letter_list)
    final_list1=[] 
    final_string = " "
    final_list = text.split()
    
    for letter in letter_list:
        num_letter = str(alpha_dict[letter])
        final_list1.append(num_letter)
        final_string = final_string +num_letter +", "

    print(final_list1)
    print(final_string)
    return final_list1

print(alphabet_position("What's up guys"))