#Concatenate two list in the following order
list1 = ["Hello","take"]
list2 = ["Dear","Sir"]

#Expected result:
#['Hello Dear','Hello Sir','take Dear','take Sir']

for i in list1:
    for j in list2:
        print(i+j)\
        