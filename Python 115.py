def maxm(n):
    arr = [-1, n, -1]
    
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0: current = x
        else: current += x
        if current > best: best = current
    return best


input("maxm(n) finds the max subarray sum in [-1, n, -1]. Press Enter")
print(" maxm(3) =", maxm(3))
print(" maxm(4) =", maxm(4))
n = int(input("Enter n (try 5 or 6)"))
guess = input("What is maxm(" + str(n) + ")?")
input("negative at start resets - best locks in the peak value n. Press Enter")
print(" maxm(" + str(n) + ") =", maxm(n),"your guess:", guess)