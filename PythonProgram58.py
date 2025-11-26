#Display Fibonacci series up to 10 terms. The Fibonacci Sequence in a series of numbers.The next number is found by adding up the two 
#numbers before it. The first two numbers are 0 and 1.
#For example, 0,1,1,2,3,5,8,12,21. The numbers in this series above is 13+21=34.
n=int(input("Enter th number: "))
num1=0
num2=1

print(num1,end=" ")
print(num2,end=" ")

for i in range(0,n):
    num3=num1+num2
    num1=num2
    num2=num3

    print(num3,end=" ")

