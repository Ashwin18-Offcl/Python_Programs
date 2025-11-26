#Remove empty strings from a list of strings
#Original list of string
#['Emma','jon'',kelly',None, 'Eric','']
#After removing empty strings
#['Emma', 'Jon','Kelly','Eric']

str_list = ["Emma","jon","","kelly",None,"Eric",""]

for i in str_list:
    if i =="" or i==None:
        str_list.remove(i)
print(str_list)