#first set is subset of second set:
#True
#Second set is subset of first set€:
#First set is a superset of first set:
#True
#second set is superset of first set:
#first set:
#set()
#second set:
#{48,34,53,22,27,43,93}
#Iterate a given list and check if a given element exist as a key's values in a dictionary. If not deleted it from the list.
#roll_number = [47,64,69,37,76,83,95,97]
#Expected result-->After removing unwanted elements from list[47,69,76,97]
roll_number = [47,64,69,37,76,83,95,97]
sample_dict = {'john':47,'Emma':69,'Kelly':76,'Jason':97}
#will modify the original list
roll_number[:]=[item for item in roll_number if item in sample_dict.values()]
print(roll_number)
