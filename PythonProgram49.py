#Calculate the sum of all numbers from 1 to a given number
#Write to accept a number from a user and calculate the sum of all nmber from 1 to given number

#For example, if the entered 10 th output should be 55 (1+2+3+4+5+6+7+8+9+10)

n=int(input("Enter the number: "))

x=0

for i in range(1,n+1):
    x=x+i

print(x)