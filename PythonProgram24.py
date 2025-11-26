#Check Palindrome Number Write a Program to Check if the given number is a palindrome number.
#A palindrome is a number that is same after rverse. For example 545, is the palindrme numbers
n=int(input("Enter the Number:"))
rev_number=str(n)[::-1]

print(rev_number)

if n==int(rev_number):
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")
    