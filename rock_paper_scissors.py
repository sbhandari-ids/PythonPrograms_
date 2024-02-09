def rps(p1, p2):
    #your code here
    if p1==p2:
        return "Draw!"
    if p1=='rock':
        if p2 == 'paper':
            return "Player 2 won!"
        else:   return "Player 1 won!"
        
    elif p1=='paper':
        if p2=='scissors':
            return "Player 2 won!"
        else: return "Player 1 won!"
        
    elif p1=='scissors':
        if p2=='rock':
            return "Player 2 won!"
        else: return "Player 1 won!"

abc = print(rps('scissors', 'scissors'))

