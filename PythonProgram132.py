"""Remove list write a program to remove all occurence of item 20.

list1 =[5,20,15,20,25,50,29]
Expected output
[5,15,25,50]"""

list1 = [5,20,15,20,25,50,20]

while 20 in list1:
    list1.remove(20)
print(list1)
