
def square(n):
    print("----Printing Square------")
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def increasing_traingle(n):
    print("----Printing Increasing Triangle-------")
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

def rightAngledTriangle(n):
    print("----Printing Right Angled Triangle-------")
    for i in range(n):
        for j in range(i, n):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()


if __name__ == '__main__':
    n = int(input("Enter n:").strip())
    square(n)
    increasing_traingle(n)
    rightAngledTriangle(n)