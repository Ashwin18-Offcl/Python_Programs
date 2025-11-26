""" Sort JSON keys in and with them into a file
Sort following JSON data alphabetical order of keys
sample JSON = {"id":1,"name":"value2","age":20}
Expected Output:
{
"age":29},
"id":1,
"name":"value2"
"name":"value2"
}
"""
import json
sampleJson = {"id":1,"name":"value2","age":20}
with open ("sampleJson","w") as write_file:
    json.dump(sampleJson,write_file,indent=4,sort_keys=True)
print("Done writting data into Json file")
