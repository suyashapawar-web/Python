input("XOR sign detcetion - n ^ m < 0 means different signs. Press Enter.")
print(" 4 ^ 2 =", 4 ^ 2, " same signs positive")
print(" 4 ^ -2 =", 4 ^ -2, " different signs negative")

n = int(input("Enter a number (try 5 or -3):"))
guess = input("Will " + str(n) + " ^ -8 be positive or negative?")
input("XOR is negative when when signs differ. Pres enter.")
print(" ", n," ^ -8", n ^ -8, " your guess:", guess)