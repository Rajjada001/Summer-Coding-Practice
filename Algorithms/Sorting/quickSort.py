import random

def partition(a,low,high):
    pivot = (low+high)//2 #middle element as pivot
    pivot_val = a[pivot] #store the pivot element
    # swap the pivot element with the last element
    a[high],a[pivot] = a[pivot], a[high]
    # store the smallest index as the 
    smaller_index = low

    for i in range(low,high):
        if a[i]<=pivot_val:
            a[i],a[smaller_index] = a[smaller_index],a[i]
            smaller_index+=1
    a[smaller_index],a[high] = a[high],a[smaller_index]

    return smaller_index
    # pivot = a[high]
    # i = low-1

    # for j in range(low,high):
    #     if a[j]<pivot:
    #         i+=1
    #         a[i],a[j] = a[j],a[i]
    
    # a[i+1],a[high] = a[high],a[i+1]
    # return (i+1)

def quicksort(a, low, high):
    if low<high:
        part = partition(a,low,high)
        quicksort(a,low,part-1)
        quicksort(a,part+1, high)
        return a

a = [random.randint(0,100) for _ in range(15)]
print(a)
s_a = quicksort(a, 0,14)
print(s_a)
if s_a == sorted(a):
    print(True)
else:
    print(False)

