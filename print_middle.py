import random
WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")
s = random.choice(WORDS)


def get_middle(s):
    lenn = int(len(s))
    print(f'the length of chosen string {s} is {lenn}')

    if lenn % 2 == 0:
        middle = lenn//2
        print(f'middle = {middle}')
        return s[middle-1:middle+1]
        print(middle, s[middle-1:middle+1])
    else: 
        middle = lenn//2 +1
        print(f'middle = {middle}')
        return s[middle-1] # middle-1 because the position 5 is index# 4
        print(middle, s[middle])


print(get_middle(s))