#Append new string in the middle of a given string
#Given two srings.s1 and s2. Write a program to create a new string s3 by appending s2  in the middle of s1.
#s1 = "Ault"
#s2 = "Kelly"
#xpected -->aukellylt
s1 = "Ault"
s2 = "kelly"

l = len(s1)
mid=1//2

f=s1[:mid]
s=s1[mid:]

s3=f+s2+s

print(s3)
