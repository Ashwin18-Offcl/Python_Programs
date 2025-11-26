#Remove duplicates from a list and create a tuple and find the minimum and maximum number
#sample_list = [87,45,41,65,94,41,99,94]
#Expected-->
#unique items[87,45,41,65,99]
#tuple(87,45,41,65,99)
#min:41
#max:99

sample_list = [87,45,41,65,94,41,99,94]
list1=set(sample_list)
#removed all the duplicates
tuple1=tuple(list1)
print("Unique element in the sample list:\n",tuple1)
print("Maximum number in the sample list:\n",max(tuple1))
print("Minimum number in the sample list:\n",min(tuple1))
