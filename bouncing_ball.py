def bouncing_ball(h, bounce, window):
    
    if h < 0 or  bounce > 1 or bounce < 0 or window > h : return -1
    else : 
        i = 1
        keep_bouncing = True
        while(keep_bouncing != False):
            
            bounce_i = h*bounce
            print(f'height = {h}, bounce = {bounce}, window = {window} bounce_count = {i} bounce_height = {bounce_i}')
            h = bounce_i
            if window > h:
                keep_bouncing = False
                break
            else:  
                i+=1   
            
        return(i-1)*2 +1
    
print(bouncing_ball(30, 0.75, 1.5))



def bouncing_ball(h, bounce, window):
    
    if h < 0 or  bounce > 1 or bounce < 0 or window > h : return -1
    else : 
        i = 1
        keep_bouncing = True
        while(keep_bouncing != False):
            
            bounce_i = h*bounce
           # print(f'height = {h}, bounce = {bounce}, window = {window} bounce_count = {i} bounce_height = {bounce_i}')
            h = bounce_i
            if window > h:
                keep_bouncing = False
                break
            else:  
                i+=1   
            
        return (i-1)*2 +1