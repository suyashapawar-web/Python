def romanToInt(rInput):
    r = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5} 

    rInteger = 0
    # Go from 0 to len-1 if integer equivalent is greater than next element then add it else subtract it
    for i in range(0, len(rInput) - 1):
        if r[rInput[i]] < r[rInput[i + 1]]:
            rInteger -= r[rInput[i]]
        else:
            rInteger += r[rInput[i]]
    return rInteger + r[rInput[- 1]]

r = input("Input roman numeral:")
print("Integer equivalent =", romanToInt(r))