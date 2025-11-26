#Print downward half-Pyramid Pattern wih star (astrisk)
n=int(input("Enter the number: "))

for i in range(n+1,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print("\n")
    