"""PYTHOIN SET EXERCISE WITH SOLUTION"""
"""Add a list of elements to a set
Given a Python list,write a program to add all its elements into a given set.
sample-set={"Yellow","Orange","Black"}
sample-list=["Blue","Green","Red"]"""
sample_set = {"Yellow","Orange","Black"}
sample_list = ["Blue","Green","Red"]

sample_set.update(sample_list)
print(sample_set)
