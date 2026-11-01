def maxf(n):
    arr = [1]*n + [-1]
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current += x
        if current > best: best = current
    return best

input("maxf(n) finds the max subarray sum in [1, 1, ..., 1, -1]. Press Enter")
print(" maxf(3) =", maxf(3))
print(" maxf(4) =", maxf(4))
n = int(input("enter n (try 5 or 6)"))
guess = int(input("What is maxf(" + str(n) + ")"))
input("best locks in n ones - the last -1 drags sum down but best holds. Press Enter")
print(" maxf(" + str(n) + ") =", maxf(n)," your guess:", guess)