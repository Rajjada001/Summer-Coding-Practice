# Enter your code here. Read input from STDIN. Print output to STDOUT
def checkIfExists(d, first_name):
    res = []
    for key in d:
        if key == first_name:
            res.append(key+'='+int(d[key]))
        else:
            res.append("Not found")
    return res

t = int(input())
for _ in range(t):
    d = dict(input().split())
    first_names = []x
    first_names.append(input())
    result = checkIfExists(d, first_names)
    for res in result:
        print(res)