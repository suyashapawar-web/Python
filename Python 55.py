
def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)] # Initialize list for numbers 0 to num
    prime[0] = False # 0 is not a prime number
    prime[1] = False # 1 is not a prime number
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            # Update all multiples of p greater than or equal to p*p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    for p in range(10, num + 1):
            if prime[p]:
                print(p)
SieveOfEratosthenes(99)