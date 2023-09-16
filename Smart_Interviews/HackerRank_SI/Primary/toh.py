
def toh(n, src, temp, dest):
    if n==0:
        return
    toh(n-1, src, dest, temp)
    print("Move {0} from {1} to {2}".format(n,src, dest))
    toh(n-1, temp, src, dest)
    
t = int(input())
for _ in range(t):
    n = int(input())
    moves = 2**n - 1
    print(moves)
    toh(n, "A", "B", "C")
