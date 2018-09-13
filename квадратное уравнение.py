print ("Enter a,b and c to find x")
print ("a: ")
a = float(input())
print ("b: ")
b = float(input())
print ("c: ")
c = float(input())

D = b**2 - 4*a*c

if D<0:
    print("DisskremeNANT OTRITSATELNIY")
elif D == 0:
    x = -d / (2*a)
    print(x)
else:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print(x1)
    print(x2)

input()
