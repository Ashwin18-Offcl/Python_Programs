#Find the factorial of a given number Write a program to use the loop to find the factorial of a given number.
#The factorial(symbol:) mens to multiply all whole numbers from the chosen numbersdown to 1.
n=int(input("Enter the number: "))

fact=1

for i in range(1,n+1):
    fact=fact*i
print(fact)
