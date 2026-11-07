def eql(n):
    arr = [1]*n + [n] + [1]*n
    size = len(arr)
    for i in range(size):
        lefts = 0
        rights = 0
        for j in range(i):
            lefts += arr[j]
        for k in range(i + 1, size):
            rights += arr[k]
        if lefts == rights:
            return i
    return -1

n = int(input("Enter n (try 5 or 6):"))
guess = input("What is eql(" + str(n) + ")?")
print(" eql(" + str(n) + ") =", eql(n),"    your guess =", guess)