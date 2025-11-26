#User will provide 2 numbers you have to find the HCF of those 2 numbers
x=int(input("Enter the number: "))
y=int(input("Enter the number: "))

x_div=[]
y_div=[]

for i in range(1,x+1):
    if x%i==0:
        x_div.append(i)

for i in range(1,y+1):
    if y%i==0:
        y_div.append(i)

comman_list=[]

for i in x_div:
    if i in y_div:
        comman_list.append(i)

print("HCF pf given two number is ",max(comman_list))