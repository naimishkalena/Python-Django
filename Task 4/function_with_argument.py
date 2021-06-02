# Function Without Argument

def Function1():
    print('My Name Is Naimish Kalena')


Function1()
Function1()


# Function With Argument

def Function2(name):
    print('Name is :', name)


Function2('Naimish Kalena')


# Example With Return Statement

def Function3(a):
    return a


a = Function3('Naimish Kalena ')
print(a)


# Example With Multiple Return Statement

def Function4():
    name1 = 'Naimish Kalena '
    contact = 7625321546
    return name1, contact


name1, contact = Function4()
print('Name :', name1)
print('Contact :', contact)


# Default Arguments Example

def ex(b=10, c=20):
    print(b + c)


ex(30, 50)
ex()


# Keyword Arguments

def ex1(x, y):
    print('Sum Is :', x + y)

ex1(y=50, x=30)


# Variable Length Arguments

def add(*number):
    sum = 0

    for n in number:
        sum = sum + n
    print("Sum :", sum)

add(10, 30)
add(10, 30, 50)

#Example With Keyword Arguments

def func(**arg):
    for i,j in arg.items():
        print(i,j)

func(Name ='Naimish',Lastname = 'Kalena')

#Scope Of Variables

def Function5():
    v=10
    print('Value Inside Function :',v)

z=15
Function5()
print('Value Outside Function :',z)

#Modules In Python

import mymodule

name =mymodule.nk("Naimish")
print(name)

#Arithmetic Operator

m=10
n=7

print('M+N : ',m+n)
print('M-N : ',m-n)
print('M*N : ',m*n)
print('M/N : ',m/n)
print('M//N : ',m//n)
print('M**N : ',m**n)

#Comparison Operators

d = 20
e = 12

print('d > e is ', d > e )
print('d < e is ', d < e )
print('d == e is ', d == e )
print('d != e is ', d != e )
print('d >= e is ', d >= e )
print('d <= e is ', d <= e )

#Logical Operators

#Example of And
a1=10
a2=20
a3=30

if a1>a2 and a1>a3:
    print('A1 is the largest number.')
if a2>a1 and a2>a3:
    print('A2 is largest number.')
if a3>a1 and a3>a2:
    print('A3 is largest number.')

#Example Of Or

ch = input("Enter a character : ")

if(ch=='A' or ch=='a' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    print(ch,'Is a Vowel')
else:
    print(ch,'Is a consonant')

#membership operators

b1=10
b2=7
list2=[10,20,30,40,50]

print(b1 in list2)
print(b2 in list2)
print(b2 not in list2)

#Identity Operators
c1=20
c2=20

print(c1 is c2)
print(c1 is not c2)