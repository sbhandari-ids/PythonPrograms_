lines=['a', 'b', 'c']

def number(lines):
    #your code here\=
    new_lines = []
    for index in range(len(lines)):
        lines[index]= str(index+1) + ": " + lines[index]
        #new_lines.append(lines[index])
        
    return lines

print(number(lines))


