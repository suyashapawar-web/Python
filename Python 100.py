def minielements(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp

def maxelements(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
    return temp

a = [1234, 1, 67, 456, 29]
size = len(a)
print("a =", a)
print("Maximum element of a =", maxelements(a, size))
print("Minimum element of a =", minielements(a, size))