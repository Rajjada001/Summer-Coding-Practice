def wvc(s):
    s = s.lower()
    words = v = c  = 0
    isWord = False
    
    for char in s:
        if char.isalpha():
            if not isWord:
                words += 1
                isWord = True
            
            if char in ['a','e','i','o','u']:
                v+=1
            else:
                c+=1
        else:
            isWord = False
            
            
    return [words, v, c]

t = int(input())
for _ in range(t):
    s = input()
    words,v,c = wvc(s)
    print(words,v,c)