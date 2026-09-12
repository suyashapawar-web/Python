print("XOR exchange value.")
print("Before: a = 2, b = 5")
a = 2
b = 5
a ^= b;b ^=a;a ^=b
print("After: a =", a," b = ",b)

n = int(input("Enter a number."))
guess = input("What is n if " + str(n) + " swapped values with 8.")
a, b = n, 8
a ^= b;b ^=a;a ^=b
print("Answer:", a," Your guess:", guess)
