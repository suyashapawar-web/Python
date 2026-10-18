def totalp(n):
    prices = [1, n, 1, n, 1]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[1] - prices[i - 1]
    return profit

input(" totalp(n) sums every up swinf in prices [1, n, 1, n, 1]. Press Enter")
print(" totalp(3) =", totalp(3))
n = int(input("Enter n (try 6 or 7):"))
guess = input("What is totalp(" + str(n) + ")")
print(" add every positive step - two peaks each contribute n - 1")
print(" totalp(" + str(n) + ") =", totalp(n), " guess =", guess)