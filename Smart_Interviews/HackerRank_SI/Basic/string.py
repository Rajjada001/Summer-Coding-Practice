
def ascii(s):
    c = [0 for i in range(26)]
    for i in range(len(s)):
        c[s[i] - 97]+=1
        c[s[i] - 'a'] += 1
    return c

def frequency(s):
    c = [False for _ in range(26)]
    for i in range(len(s)):
        val = ord(s[i]) - ord('a')
        # print(val)
        if not c[val]:
            c[val] = True
        else:
            return s[i]
    return -1
def toggle(s):
    ans = ""
    for i in range(len(s)):
        ans += chr(ord(s[i])^32)
        # print(c)
    return ans
    

s = input()
# ascii(s)
# print(frequency(s))
print(toggle(s))