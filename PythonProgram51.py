#Display numbers from a list using loop Write a program to display only the numbers from a list that satisfy the following condition
#The number must be following conditions
#The number must be divisible y five
#If the number is greater than 150, then skip it and move ti the next number
#if the number is greater than 500, then stop the loop

num=[12,75,150,180,145,525,50]

for i in num:
    if i>500:
        break
    elif i>150:
        continue
    else:
        if i%5==0:
            print(i)