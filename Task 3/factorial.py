#logic of factorial is n*(n-1) and run the loop till 0

n = int(input("Enter the number you want the factorial of : "))
fact = 1

for i in range(n,0,-1):
    fact*=i

print("factorial of ",n ,"is ",fact)





