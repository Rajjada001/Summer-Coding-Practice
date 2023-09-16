def isAnagram(a,b):
    countA = [0]*26
    countB = [0]*26
    if len(a)!=len(b):
        return False
    for char in a:
        countA[ord(char)-ord('a')] += 1
    for char in b:
        countB[ord(char)-ord('a')] += 1
    # print(countA, countB)
    for i in range(26):
        if countA[i] != countB[i]:
            return False
    return True

t = int(input())
for _ in range(t):
    a,b = map(str, input().split())
    print(isAnagram(a,b))