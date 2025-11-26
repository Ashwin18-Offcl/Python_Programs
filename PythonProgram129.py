"""Remove empty strings from the list of strings
list1 = ["Mike","","Emma","Kelly","","Brad"]
expected 
["Mike","Emma","Kelly""Brad"]
"""
list1 = ["Mike","","Emma","Kelly","","Brad"]
result=list(filter(lambda x: x!="",list1))
print(result)
