"""Extend nested list by adding the  sublist
You have given a nested list. Write a program to extend it by adding the sublist["h","i","j"] in such a way that 
it  will look like the following list.
list = ["a","b",["c",,["d","e",["f","g"],"k"],"m","n"]
sub list to add su8b_list = ["h","i","j"]
Expected Result:
["a","b",["c",["d","e",["f","g","h","i","j"],"k"],"m","n"]
"""

list1 = ["a", "b", ["c", "e", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][2][2].extend(sub_list)
print(list1)
