def isPrime(n):
    p = 0
    if n<=1:
        return "No"
    
    i = 2
    while i*i <= n:
        if n%i == 0:
            return "No"
        i+=1
    return "Yes"

def sieveOfErestonesis(n):
    primes = [True]*(n+1)
    # print(primes)
    for i in range(2,n+1):
        if primes[i]==True:
            for j in range(i*i,n+1, i):
                print(primes,j)
                primes[j]=False
    
    for i in range(n):
        if primes[i]==True:
            print(i, end=" ")
    print()


n = int(input())
# print(isPrime(n))
sieveOfErestonesis(n)