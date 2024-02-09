# ---------- String Tracker ----------
# DESCRIPTION:
# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.
# If no occurrences can be found, a count of 0 should be returned.
# EXAMPLES
# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0
# str_count("Hello", 'o'); // returns 1
# str_count("Hello", 'l'); // returns 2
# str_count("", 'z'); // returns 0


def string_tracker(string, charc):
    string = [*string.lower()]
    print(string)
    
    count = 0; 
    for letter in string:
        if letter == charc:
            count+=1
   
    return count

 abc = list(lambda count: count+=1 for letter in string if letter == charc)

print(string_tracker("lazy dog jumped over the brown fox", "l"))