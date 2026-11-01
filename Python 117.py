def maxa(n):
    arr = [-n] + [1]*n
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current += x
        if current > best: best = current
    return best

input(" maxa(n) finds the max subarray sum in [-n, 1, 1, ..., 1]. Press Enter")
print(" maxa(3) =", maxa(3))
print(" maxa(4) =", maxa(4))
n = int(input("Enter n (try 5 or 6):"))
guess = input("What is maxa(" + str(n) + ")?")
input("big negative resets - then n ones add up to n. Press Enter")
print("maxa(" + str(n) + ") =", maxa(n)," your guess =", guess)