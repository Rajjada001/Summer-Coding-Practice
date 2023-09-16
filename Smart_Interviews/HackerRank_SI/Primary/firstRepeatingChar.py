def firstRepeatingLeft(s):
    hm={}
    for char in s:
        if char in hm:  
            hm[char]+=1
        else:
            hm[char]=1

    for key in hm:
        if hm[key]>1:
            return key
    return '.'

def firstRepeatingRight(s):
    count = [0]*26
    for char in s:
        count[ord(char)-ord('a')]+=1
        if count[ord(char)-ord('a')]>1:
            return char
    return '.'

t = int(input())
for _ in range(t):
    s = input()
    # print(firstRepeatingLeft(s))
    print(firstRepeatingRight(s))
