#Remove and add item in a list
#Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
#sample_list=[34,54,67,89,11,43,94]
#List After removing  element at index 4[34,54,67,89,43,94]
#List After adding element at index 2[34,54,11,67,89,43,94]
#List after adding element at last[34,54,11,67,89,43,94,11]
list1 = [34,54,67,89,11,43,94]
list1.pop(4)
list1.insert(2,11)
list1.append(11)

print(list1)

