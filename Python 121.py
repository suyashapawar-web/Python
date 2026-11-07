def wins(n):
    arr = [0]*n + [1]*n
    size = len(arr)
    for i in range(size - n + 1):
        curr = 0
        for j in range(i, i + n):
            curr += arr[j]
        if curr == n:
                return i
    return -1

n = int(input("Enter n (try 5 or 6):"))
guess = input("What is wins(" + str(n) + ")?")
print("  wins(" + str(n) + ") =", wins(n), "    your guess =", guess)