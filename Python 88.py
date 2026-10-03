def flipnum(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flipnum(num // 10)
    return last * pow(10, len(str(rest))) + rest

input("flipnum peels last digit with % 10 then recurses on // 10. Press Enter")
print(" flipnum(123) =", flipnum(123))
print(" flipnum(456) =", flipnum(456))

n = int(input("Enter a number"))
guess = input("What is flip " + str(n) + " ?")
input("flipnum peels last digit and places it at the front each step. Press Enter")
print(" flipnum(" + str(n) + ") =", flipnum(n), "your guess")