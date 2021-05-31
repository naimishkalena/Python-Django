#printing smallest number using logical opreator
a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))


if a < b and a < c :
    print(a, "is the smallest")
elif (b <= a and b <= c):
    print(b, "is the smallest")
else:
    print(c, "is the smallest")