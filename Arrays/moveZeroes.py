def moveZeroes(a):
    count = 0
    for num in a:
        if num == 0:
            count += 1
            a.remove(num)
            
    while count > 0:
        a.append(0)
        count -= 1

    return a

a = [1,0,1,0,0,2,0,3,0]
print(moveZeroes(a))