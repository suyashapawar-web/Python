def maxz(n):
    arr = [1] + [0]*n + [1]
    streak = best = 0
    for x in arr:
        if not x: streak += 1
        else: streak = 0
        if streak > best: best = streak
    return best


input("maxz(n) finds the longest run of 0s in [1, 0..0, 1]. press enter")
print(" maxz(3) =", maxz(3))
print(" maxz(4) =", maxz(4))
n = int(input("Enter is maxz(try 5 or 6)?"))
guess = input("What is maxz(" + str(n) + ")?")
input("streak resets to 0 on each 0 - best keeps the highest streak seen. Press Enter")
print(" maxz(" + str(n) + ")", maxz(n), " your guess =", guess)