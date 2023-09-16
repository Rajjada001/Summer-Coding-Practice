
def selectionSort(a):
    for i in range(len(a)):
        min_index = i
        for j in range(i+1, len(a)):
            if a[j]<a[min_index]:
                a[i],a[j] = a[j],a[i]
    return a



import random
a = [random.randint(0,100) for _ in range(15)]
s_a = selectionSort(a)
if s_a == sorted(a):
    print(True)
else:
    print(False)