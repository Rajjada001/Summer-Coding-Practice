def enclosingSubstr(A, B):
    count = [0] * 256
    for char in A:
        count[ord(char)] += 1
    
    left = right = 0
    minLen = float('inf')
    minStart = -1
    countSize = len(A)
    
    while right < len(B):
        if count[ord(B[right])] > 0:
            countSize -= 1
        count[ord(B[right])] -= 1
        right += 1
        
        while countSize == 0:
            if right - left < minLen:
                minLen = right - left
                print("ML:", minLen)
                minStart = left
            
            count[ord(B[left])] += 1
            if count[ord(B[left])] > 0:
                countSize += 1
            left += 1
    
    if minStart == -1:
        return -1
    return minLen

# Test cases
t = int(input())
for _ in range(t):
    A,B = map(str, input().split())
    print(enclosingSubstr(A,B))

# t = int(input())
# for _ in range(t):
#     A,B = map(str, input().split())
#     print(enclosingSubstr(A,B, len(A), len(B)))