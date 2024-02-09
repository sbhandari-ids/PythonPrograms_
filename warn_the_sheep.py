def warn_the_sheep(queue):
    animal_count = len(queue)
    index = 0

    for animal in queue : 
        index +=1
        if animal == 'wolf':
            wolf_position = index 

    sheep_in_danger_position = animal_count - wolf_position
    if wolf_position == animal_count : 
        message = "Pls go away and stop eathing my sheep" 
    else : message = "Oi ! Sheep number "+ str(sheep_in_danger_position) +" ! You are about to be eaten by a wolf!" 

    return message   
     
         
message1 = print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))

message1= print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'wolf']))

message3 = print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))

#message4= print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep']))

      