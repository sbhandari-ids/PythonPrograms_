
    
def is_it_a_num(s: str) -> str:
    x = list(s.strip(" "))
    phone_num=""
    for letter in x:
        if letter.isnumeric():
            phone_num+=letter
            
    print(phone_num)
    print(len(phone_num))
    print(phone_num[0])

    if len(phone_num)==11:
        if phone_num[0]==0:
            result = phone_num
        else: result ="Not a phone number"
        
    return result

y= print(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"))