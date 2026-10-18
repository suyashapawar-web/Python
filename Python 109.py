def rn(n):
    bars = [0, n, 0, n, 0]
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

input("rn(n) traps water between two bars of height n. Press Enter")
print(" rn(3) =", rn(3))
n = int(input("Enter bar height"))
guess = input("What is rn(" + str(n) + ")?")
print("water = min(left_tallest, right_tallest) - bar height at the gap")
print(" rn(" + str(n) + ") =", rn(n), "guess =", guess)