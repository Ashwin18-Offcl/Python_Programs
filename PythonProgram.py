#Swap the number without using third variable
x=int(input("Enter the first number"))
y=int(input("Enter the Second number"))

print(x,y)

x=x+y
y=x-y
x=x-y

print(x,y)
