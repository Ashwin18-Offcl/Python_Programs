#Write a program that keeps on accepting a number rom the user user enters Zero.
#Display the sum and average of all the numbers.
n=int(input("Enter the number: "))

total=0
avg=0
count=0

while True:
    if n !=0:
        total=total+n
        count +=1
        avg=total/count
        n=int(input("Print another number: "))
    else:
        print("Thank you")
        break
print("your sum is :",total)
print("your avg is :",round(avg,2))
