#Create a fuction with vaiable leggth of arguments
#Write a program to create  fuction fucn1() to accept a variable length of arguments and print their value.
#Note Create a function in such a way that we can pass that we can pass any number of argument to this function, and the function should  process them and display ech arguments value
def inputs(*num):
    """Function to return the given numbers as a tuple"""
    return num

# Example usage
print(inputs(45, 67, 78))
