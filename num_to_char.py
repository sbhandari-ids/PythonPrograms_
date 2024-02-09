def correct(s):
    s_arr[] = s.split()
    print(s_arr)
    for position in range(len(s_arr)):
        if s_arr[position] == '5':
            s_arr[position] = 'S'
        elif s_arr[position] == '0':
            s_arr[position] = 'O'
        elif s_arr[position] == '1':
            s_arr[position] = 'I'
            
    return s_arr

abc = correct("L0ND0N")

