#Find th interaction (common) of two sets nd remove those element from the firt set
#first_set = {23,42,65,57,78,83,29}
#second-set={57,83,29,67,73,43,48}
#Intersectio is{57,83,29}
#First Set after rmoving common element {65,42,78,23}

first_set = {23,42,65,57,78,83,29}
second_set = {57,83,29,67,73,43,48}
intersection=first_set.intersection(second_set)

print(intersection)
for i in intersection:
    first_set.remove(i)
print(first_set)
