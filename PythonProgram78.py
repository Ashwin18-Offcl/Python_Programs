#Create a recursive function
#A] Write a program to create a recursive function to calculate the um of numbers from 0 to 10.
#A recursive functio is a function that calls itself again and again.
def addition(num):
    if num < 0:
        raise ValueError("Input must be a non-negative integer")
    if num == 0:
        return 0
    return num + addition(num - 1)

# Example usage:
print(addition(5))  # Output: 15