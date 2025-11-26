#Create a string made of the middle three charactrs
#Write a program to create a new string made of the middle three character of an input string.
#ex.JaSonAy-->Son
#jhonDippeta-->Dip
name = "JaSonAy"
l = len(name)
if 1%2==0:
    print("not possible")
else:
    c=2//2
    x=name[c-1]
    y=name[c]
    z=name[c+1]

    result="".join([x,y,z])

    print(result)
    