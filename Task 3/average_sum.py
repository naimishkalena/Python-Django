n = int(input("Enter Number to calculate sum & average : "))

sum = 0

for num in range(0, n + 1, 1):
    sum+=num

average = sum / n

print("SUM of", n, "numbers is: ", sum)
print("Average of", n, "natural number is: ", average)