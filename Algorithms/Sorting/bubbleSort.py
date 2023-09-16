
def bubbleSort(a):
    for i in range(len(a)):
        swapped = False
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
        if swapped == False:
            break
    return a
# def bubbleSort(a):
    # for i in range(len(a)):
    #     for j in range(i,len(a)):
    #         if a[i]>a[j]:
    #             a[i],a[j] = a[j],a[i]
    # return a

import random
a = [random.randint(0,100) for _ in range(15)]
s_a = bubbleSort(a)
if s_a == sorted(a):
    print(True)
else:
    print(False)


