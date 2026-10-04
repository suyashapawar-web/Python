def countparen(n, l=0, r=0):
    if l == n and r == n:
        return 1
    total = 0
    if l > r:
        total += countparen(n, l , r + 1)
    if l < n:
        total += countparen(n, l + 1, r)
    return total

input("countparen counts every valid {} sequence - returns 1 at each valid end. Press Enter")
print(" countparen(3) =", countparen(3))


n = int(input("Enter a number of pairs(try 5 or 6):"))
guess = input("What is countparens("+ str(n) + ")")
print(" countparen(" + str(n) + ") =", countparen(n), "     your guess:", guess)