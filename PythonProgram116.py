#Checks if one set is a subset or superset of another.If found. delete all elements from that set
#first_set={27,43,34}
#second_set={34,93,22,27,43,53,48}
#expected output:
#first set is subset of second set - True
#Second set is subset of First set - False
#First set is Super set of second set - False
#Second set is Super set of  First set-True
#First Set set()
#Second Set {67,73,43,48,83,57,29}

first_set = {27, 43, 34}  # Changed from list to set
second_set = {34, 93, 22, 27, 43, 53, 48}

print("first set is subset of second set:\n", first_set.issubset(second_set))
print("second set is subset of the first set:\n", second_set.issubset(first_set))
print("first set is superset of second set:\n", first_set.issuperset(second_set))
print("second set is superset of first set:\n", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()
print("first set:\n",first_set)
print("second set;\n",second_set)

