#Write a program to print all the unique combination of two digits from 1 to 4 for ex (1,2), (2,3)....
#since e have 4 digit there unique combination will be 16
x=int(input("Enter the number: "))

new=[]

if x==1:
    print("1 is not prime number")
else:
    for i in range(1,x+1):
        if x%i==0:
            new.append(i)
            #print(new)

        if len(new) > 2:
            print("it is not a prime number")
        else:
            print("it is prime number")
            