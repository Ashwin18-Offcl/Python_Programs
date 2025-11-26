#Arrange strng character such that lowercase letters should come first 
#Given string cntains a combination of the lower and upper case letters. Write a program to arrange the character of a string so that all lowercase letter should come first.
#given-->PyNaTive
#epected-->yaive PNT
string="PyNaTive"
cap=list(string.upper())
sma=list(string.lower())

new=[]

l1=list(string)

for i in l1:
    if i in sma:
        new.append(i)
for i in l1:
    if i in cap:
        new.append(i)
result="".join(new)
print(result)
