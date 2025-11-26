#Return multiple values from a fuction
#Write a program to create function calculation() such that it can accepth two variables and calculate addition
#and subtraction Also, if must return both addition and subtraction in a single return call.
def add_sub(n1,n2):
    x1=n1+n2
    x2=n1-n2

    return x1,x2
print(add_sub(40,10))