#Printcharacter from a string that are preset at an even index number Write a program to accept a string from the user and dislplay characters that are 
#present at an even index number.
#or example, sir str="pynative" so you should display 'p','n','t','v'
string=input("Enter the text: ")
x=list(string)

print(string)

for i in x[0::2]:
    print(i,end=" ")
    