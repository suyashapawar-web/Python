num = int(input("Enter a number:"))
digits = len(str(num))
temp = num
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers+= digit ** digits
    temp //= 10
if sum_of_powers == num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")