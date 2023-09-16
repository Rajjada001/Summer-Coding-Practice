'''
Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
The mergeSort() function is used for merging two halves.
```
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
```
'''


# def MergeSort(a):
#     if len(a) > 1:
#         mid = len(a)//2
#         left = a[mid:]
#         right = a[:mid]
#         MergeSort(left)
#         MergeSort(right)

#         i=j=k=0
#         # print("Before While")
#         while i<len(left) and j < len(right):

#             if left[i]<=right[j]:
#                 a[k] = left[i]
#                 i += 1
#             elif left[i] > right[j]:
#                 a[k] = right[j]
#                 j += 1

#             k += 1

#         # Remaining elements
#         while i < len(left):
#             a[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             a[k] = right[j]
#             j += 1
#             k += 1

#     return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i = 0  # Pointer for the left sublist
    j = 0  # Pointer for the right sublist

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Example usage
arr = [5, 2, 8, 3, 1, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)
