def maxones(n):
    arr = [1]*n + [0] + [1]*n
    streak = best = 0
    for x in arr:
        if x: streak += 1
        else: streak = 0
        if streak > best: best = streak
    return best


input("maxones(n) finds the longest run of 1s in [1..1, 0, 1..1]. press enter")
print(" maxones(3) =", maxones(3))
print(" maxones(4) =", maxones(4))
n = int(input("Enter is maxones(try 5 or 6)?"))
guess = input("What is maxones(" + str(n) + ")?")
input("streak resets to 0 on each 0 - best keeps the highest streak seen. Press Enter")
print(" maxones(" + str(n) + ")", maxones(n), " your guess =", guess)