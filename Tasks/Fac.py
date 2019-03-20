def Fac(a):
    if a >= 1:
        return Fac((a-1))*a
    else:
        return 1


x = int(input("Please enter Number\n"))

print(Fac(x))