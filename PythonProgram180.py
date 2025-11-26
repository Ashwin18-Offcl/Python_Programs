""" Python JSON(java Script Object Notation)
Exercise

Exercise 180: Convert the following dictionary into JSON format
data=("key1","value1","key2","value2")
Expected Output
data = ("key1":"value","keys2","value2")"""
import json
data = {"key1": "value1","key2":"value2"}
jsondata=json.dumps(data) #dict converted to string
print(jsondata)