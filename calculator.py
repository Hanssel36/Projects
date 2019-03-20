#Basic calulator

def Cal(a, b,c):
    if b == "*":
        return a*c
    if b == "+":
        return a+c
    if b == "-":
        return a-c
    if b == "/":
        return a/c


print()

a =  int(input('Please enter a number'))

print()

c = int(input('Please enter a number'))

print("*,+,-,/")

b = input()

print(Cal(a,b,c))