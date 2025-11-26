#Find all occurenced of a substring in a given string by ignoring the case Write a program to find all occurrence of "USA" in a given ignoring the case.
#str1 = "Welcome to "USA". usa awesome,isn't it?
#expected an --> USA :-->2

str1 = "Welcome to USA. usa awesome, isn't it?"

str2=str1.upper()
print(str2)

str2.count("USA")


