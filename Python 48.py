# Keep input as a string to allow slicing
num = input("Enter binary numbers: ")

decimal = 0
power = 0

# Now slicing works perfectly
for digit in num[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal equivalent:", decimal)
