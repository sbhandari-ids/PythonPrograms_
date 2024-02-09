# def check_element(x):
#     list1 = ['a', 'boy', 'zoe', 5, 9, 21]
#     match = False
#     for item in list1:
#         if item.isalpha():
#             if item.lower() == str(x).lower():
#                 match = True
        
#         elif item == x: 
#                 match = True 
    
#     return match

# in_array_element = print(check_element('a'))


def check_element(list1, x):
    #list1 = ['a', 'boy', 'zoe', 5, 9, 21]
    match = False
    for item in list1:
        if  item == x: 
            match = True 
       
    
    return match

in_array_element = print(check_element(['a', 'boy',110, '!', 'zoe', 5, 9, 21], '!'))
