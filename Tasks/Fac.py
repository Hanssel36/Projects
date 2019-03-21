def Fac(a):
    if a == 0:
        return 1
    else:
        return Fac((a-1))*a


x = int(input("Please enter Number\n"))

print(Fac(x))