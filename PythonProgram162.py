"""Check if all items in the tuple are the same
tuple1 = (45,45,45,45)"""
t = (45,45,45,45)
#to check wherther all the items are same
all_same = all (i==[0] for i in t)
if all_same:
    print("yea all the item are same in the given tuple")
else:
    print("No all the item are not same in the given table")
    #error show
    