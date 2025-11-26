#Write a program to create a recursive fuction to calculation the factorial of numbers from 0 to 10.
#A recursive function is a function that calls itself again and again.
def factorial(num):
    if (num==1):
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))