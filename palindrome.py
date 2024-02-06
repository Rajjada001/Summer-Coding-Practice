def palindrome(s):
    s = ''.join([x for x in s.lower() if x.isalnum()])
    return s==s[::-1]

s = "A man, A plan, A canal: Panama"
print(palindrome(s))    