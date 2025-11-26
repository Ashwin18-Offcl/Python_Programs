#Calculate the multiplication and sum of two numbers
#Given two integers numbers retur their product only if the product is equal to or lower than 1000, else return their sum.
def mul_sum_int(num1, num2):
    """Function to return the product if it's ≤ 1000, else return sum"""
    mul = num1 * num2
    total = num1 + num2
    
    # Checking the condition
    return mul if mul <= 1000 else total

# Taking user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calling the function and printing the result
print(mul_sum_int(num1, num2))