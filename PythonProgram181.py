""" Exercise: Access the value of key2 from the following JSON
import json
samplejson = {"key1":"value1","key2":"value2"}
# write code to print the value of key2
# Expected Output:
# value2
# """
import json
sampleJson = """{"key1":"value1","key2":"value2"}"""
data=json.loads(sampleJson) #converted to dictionary
data["key2"]
print(data["key2"])