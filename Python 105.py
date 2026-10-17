def gr(n):
    arr = [1, 2, 3, 4, 5, 6]
    for i in range(0, 6, n):
        arr[i:i+n] = arr[i:i+n][::-1]
    return arr

input("gr(n) reverse [1, 2, 3, 4, 5, 6] in chunks of n. Press Enter")
print(" gr(2) =", gr(2))
n = int(input("Group size (try 1 - 6):"))
guess = input("What is gr(" + str(n) + ")?")
input("each chunk of n elements is flipped in place. Press Enter")
print(" gr(" + str(n) + ") =", gr(n), " guess:", guess)