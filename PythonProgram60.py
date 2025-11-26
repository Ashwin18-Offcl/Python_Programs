#Reverse a given integer number Given.
#76542
#Expected output
#24567
n=int(input("Enter the number: "))
x=str(n)

x=list(x)[::-1]

z=int("".join(x))
print(z)
#print(type(z))
