

def first_and_last_pos_of_element(nums, target):
        
    def search(nums, t):
        l,r = 0,len(nums)-1
        while l<=r:
            mid = l + (r-l)//2
            if a[mid]<t:
                l = mid+1
            else:
                r = mid-1
        return l
    
    res = [-1,-1]
    
    l = search(nums, target)
    r = search(nums, target+1)-1

    if l<=r:
        return [l,r]
    
    return res



# def search(a, target, findStartIndex):
#     res = -1
#     l,r = 0,len(a)-1
#     while l<=r:
#         mid = l+(r-l)//2
#         if a[mid] < target:
#             l = mid+1
#         elif a[mid] > target:
#             r = mid-1
#         else:
#             # potential answer is found
#             res = mid
#             if findStartIndex:
#                 r = mid-1
#             else:
#                 l = mid+1

#     return res


t = int(input("Enter no of test cases:"))
for _ in range(t):
    print("Enter array elements")
    a = list(map(int, input().split()))
    target = int(input("Enter target:"))
    print(first_and_last_pos_of_element(a, target))
    
