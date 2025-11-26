#Count the total number of digit in a number Write a program to count the total number of digits in a number usng a while loop.
#For example, the numbers is 75869,so the output should be 5.
n=input("Enter the number: ")

x=list(n)

count=0

while count<len(x):
    for i in x:
        count+=1
print(count)