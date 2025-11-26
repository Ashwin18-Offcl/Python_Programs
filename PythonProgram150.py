"""Check if two sets have any element in common.If yes, display the common elements 
set1 = {10,20,30,40,50}
set2 = {60,70,80,90,10}
expected:
Two sets have items in common{10}"""
set1 = {10,20,30,40,50}
set2 = {60,70,80,90,10}

if set1.isdisjoint(set2):
    print("above two sett dont have any common element")
else:
    set1.intersection(set2)
print(set1.intersection(set2))
