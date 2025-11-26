#Write a program to find the volume of the cylinder. Also find the cost when, when the cost of 1 litre milk is 40Rs.
rad=float(input("Enter the radius of cylinder in cm "))
ht=float(input("Enter the height of cylinder in cm "))

vol=3.142*(rad**2)*ht
litr=vol/1000
cost=litr*40

print("Volume of cylinder will be ",vol)
print("How much milk we can carry in this cylinder ",litr,'ltr')
print("This cost of that milk will be",cost)
