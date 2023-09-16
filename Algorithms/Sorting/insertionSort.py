import random

def insertionSort(a):
    n = len(a)
    for i in range(1, n):
        j = i-1
        key = a[i]
        while j>=0 and a[j]>=key:
            a[j],a[j+1] = a[j+1],a[j]
            j-=1
    
    return a

a = [random.randint(0,100) for _ in range(15)]
print(a)
s_a = insertionSort(a)
if s_a == sorted(a):
    print(True)
else:
    print(False)