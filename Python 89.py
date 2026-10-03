def flipname(s):
    if len(s) == 1:
        return s
    return flipname(s[1:]) + s[0]

input("flipname recurses on s[1:] then attaches s[0] at the end. Press ENter")
print(" flipname('Maya') =", flipname('Maya'))

name = input("enter a name")
guess = input(" what is flipname('" + name + "')")
input("flipname(s) = flipname(s[1:]) + s[0] first character lands last. Press Enter")
print("flipname('" + name + "')=", flipname(name),"guess", guess)