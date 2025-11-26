#Write a program to print multiplication table of a given number For example, num=2 so the output should be
n=int(input("Enter the number: "))
for i in range(1,11):
    x=n*i
    print(x,end=" ")
    