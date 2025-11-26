#Count th frequency of a particular character in a provided string.Eg'hello how are you's is the string.the frequency of h in this string is 2.
a = input("Enter the text: ")
b = input("Enter the character: ")

count=0

for i in a:
    if i in b:
        count=count+1
print("Frequency of searched character is",count,"times")
