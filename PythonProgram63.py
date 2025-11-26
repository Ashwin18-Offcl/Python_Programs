#Find the sum of the series upto n terms Write a program to calculate the sum of series up to n term. For example, if n=5 the series will
#become 2+22+222+2222+22222=24690
n=5

x=2
result=0

for i in range(1,6):
    y=str(x)*i
    z=int("".join(y))
    #print(z)
    result=result+z

#type(z)
print(result)
