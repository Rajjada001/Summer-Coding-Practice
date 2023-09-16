def generateParanthesis(arr, n, s, op, cl):
    if op==n and cl==n:
        arr.append(s)
    if op<n:
        generateParanthesis(arr,n,s+'{', op+1, cl)
    if cl<op:
        generateParanthesis(arr, n, s+'}', op, cl+1)
    
        
t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    print("Test Case #{0}:".format(i+1))
    generateParanthesis(arr, n, '', 0,0)
    for s in arr:
        print(s)