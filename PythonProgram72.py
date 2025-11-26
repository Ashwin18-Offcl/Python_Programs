#Check a function in python Write a program to create a function that takes two arguments.
#and last number of a given list is same. If numbers are different then return False.
l1=[1,2,3,4,5,1]

num1=l1[0]
num2=l1[-1]

def xyz(list):
    if num1==num2:
        return True
    else:
        return False
xyz(l1)





