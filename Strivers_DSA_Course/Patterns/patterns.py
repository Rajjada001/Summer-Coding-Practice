def square(n):
    for row in range(n):
        for col in range(n):
            print("*", end=" ")
        print()

def right_angled_triangle(n):
    for row in range(n):
        for col in range(row+1):
            print("*", end="")
        print()
def right_angled_triangle_numbers(n):
    for row in range(n):
        for col in range(row+1):
            print(row+1, end="")
        print()
def reverse_right_angled_triangle(n):
    for row in range(n):
        for col in range(row, n):
            print("*", end="")
        print()

def pyramid(n):
    for row in range(n):
        # space
        for j in range(n-row-1):
            print(" ", end="")
        # stars
        for j in range(2*row+1):
            print("*", end="")
        # space
        for j in range(n-row-1):
            print(" ", end="")
        print()

def reverse_pyramid(n):
    k = n
    for i in range(n):
        # space
        for j in range(i):
            print(" ", end="")
        # stars
        for j in range(2*k-1, 0, -1):
            print("*", end="")
        # space
        for j in range(i):
            print(" ", end="")
        k-=1

        print()

def rhombus(n):
    pyramid(n)
    reverse_pyramid(n)

def right_rotated_pyramid(n):
    # right_angled_triangle(n)
    # reverse_right_angled_triangle(n-1)
    for i in range(2*n):
        stars = i
        if i>n:
            stars = 2*n-i
        for j in range(stars):
            print("*", end="")
        print()

def zero_one_ra_triangle(n):
    start = 1
    for i in range(n):
        if i%2==0:
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start, end="")
            start = 1-start
        print()

def pattern_12(n):
    space = 2*(n-1)
    for i in range(n):
        # numbers
        for j in range(i+1):
            print(j+1, end="")
            # start = start+1
        # space
        for j in range(space):
            print(" ", end="")
        # numbers
        for j in range(i+1, 0, -1):
            print(j, end="")
            # start = start+1
        space -= 2
        print()

def right_triangle_numbers(n):
    start = 1
    for i in range(n):
        for j in range(i+1):
            print(start, end=" ")
            start+=1
        print()

def right_triangle_characters(n):
    for i in range(n):
        for j in range(ord('A'),ord('A')+i+1):
            print(chr(j), end="")
        print()
        
# square(5)
# right_angled_triangle(5)
# right_angled_triangle_numbers(5)
# reverse_right_angled_triangle(5)
# pyramid(5)
# reverse_pyramid(5)
# rhombus(5)
# right_rotated_pyramid(5)
# zero_one_ra_triangle(5)
# pattern_12(4)
# right_triangle_numbers(5)
right_triangle_characters(5)


