#first we will write code for getting prime number
a=23
new=[]
for i in range(1,a+1):
    if a%i==0:
        new.append(i)
if len(new)>2:
    print("it's not a prime number")
else:
    print("it's prime number")
