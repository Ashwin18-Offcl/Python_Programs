l1=[4,5,6,2,3,9,1,4,5,6,3]
n=int(input("Enter the numbe:"))

for i in l1:
    if i==n:
        print("Number exixt")
        break
else:
    print("Number dont exist")
    