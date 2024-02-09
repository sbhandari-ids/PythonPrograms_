import string
def check_pangram(s):
#    letter_book = []
#    for letter in s:
#      if letter != string.punctuation:
#         if letter in letter_book:
#             continue
#         elif letter.isalpha():
#             letter_book.append((letter).lower())
#    print(sorted(letter_book))

#    if len(letter_book)==26:
#       return True
#    else: return False

    if string.ascii_lowercase in s: 
        return True
    else : return False


    


print(check_pangram("abcdefghijklmnaopqrstuvwxyz"))