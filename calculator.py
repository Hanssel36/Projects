#Basic calulator

def Cal(a, b,c):
    if b == "m":
        return a*c


print('Please enter a number')

a =  input(int)

print('Please enter a number')

c = input(int)

print("*,+,-,/")

b = input()



print(Cal(a,b,c))