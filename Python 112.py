def movez(n):
    arr = [1, 0] * n
    write = 0
    for x in arr:
        if x: arr[write] = x; write += 1
    arr[write:] = [0] * (len(arr) - write)
    return arr

input("movez(n) moves all zeros to the end of [0, 1, 0, 1,....].Press Enter")
print(" movez(3) =", movez(3))
print(" movez(4) =", movez(4))
n = int(input("Enter n (try 5 or 6)"))
guess = input(" What is movez(" + str(n) + ")?")
input("write pointer collects non-zeros - fill the rest with zeros. Press Enter")
print("movez(" + str(n) + ") =", movez(n)," your guess =", guess)