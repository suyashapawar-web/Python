
def print_factors(num):
    print("The factors of", num," are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

num = (int(input("Enter a whole number:")))
if num <= 0:
    print("Enter a number greater then 0")

print_factors(num)