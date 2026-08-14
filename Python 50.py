numberL = int(input("Enter Largest number:"))
numberS = int(input("Enter Smallest number:"))

while(numberS):
    numberSt = numberS
    numberS = numberL % numberS
    numberL = numberSt

print("HCF is:", numberL)