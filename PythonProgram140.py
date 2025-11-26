"""Check if a value exists in a dictionary
We know how to check if the key exist in a dictionary Sometimes it is required to check if the given value is present
Write a Python program to check if value 200 exixts in the following dictionary.
given.
sample_dict = {'a':100,'b':200,'c':300}
expected:
200 present in a dict
"""
sample_dict = {'a':100, 'b':200,'c':300}
if 200 in sample_dict.values():
    print("200 present in given dict")
    