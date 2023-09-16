def sum_zero(a):
    max_sum = curr_sum = a[0]
    for i in range(1,len(a)):
        curr_sum = a[i] + a[i-1]
        curr_sum = max(curr_sum, 0)
        max_sum = max(0, curr_sum)

    return max_sum

n = int(input("Enter no of test cases"))
for _ in range(n):
    print("Enter Array elements")
    a = list(map(int, input().split()))
    print(sum_zero(a))