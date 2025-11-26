"""Create a dictionary by extracting thr keys from a given dictionary 
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
Sample _dict = {"name","Kelly","age",25,"salary".8000,"city"."New york"}
"key to extract keys = ["name","salary"]
expected output:
{'name':'salary':8000}"""
sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
}
keys=["name","salary"]
result=dict()
for k in keys:
    result.update({k:sample_dict[k]})
print(result)
#or using dictionary comprehension
sample_dict = {
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"New york"
}
keys = ["name","salary"]
new_dict={k:sample_dict[k] for k in keys}
print(new_dict)