"""Return a set of element present in Set  A or B, but not both
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
Expected Output:
{20,70,10,60}"""
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
set1.symmetric_difference(set2)