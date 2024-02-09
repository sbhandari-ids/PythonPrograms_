def how_much_coffee(events):
    coffee_count = 0
    for event in events:
        if event!= 'other':
            if event.isalpha():
                if event.islower():
                    coffee_count +=1
                elif event.isupper():
                    coffee_count +=2
    
    
    if coffee_count > 3:
        return "you need extra sleep"
    return coffee_count

coffee_count_ = print(how_much_coffee(['other']))
coffee_count_ = print(how_much_coffee(['othersp', 'CAT', 'dog']))