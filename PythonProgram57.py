#Write a program to display all prie numbers within a range
#Note:A Prime Number is a number which only divisible by one and number itself.but 1 is not prime number
def prime(n):
    if n<1:
        return False
    else:
        l1=[]

        for i in range(1,n+1):
            if n%i==0:
                l1.append(i)
                #print(l1)
        if len(l1)<=2:
            return True
        else:
            return False
inp1=int(input("Enter the number: "))
inp2=int(input("Enter the number: "))

for i in range(inp1,inp2+1):
    if prime(i)==True:
        print(i,end=" ")
        