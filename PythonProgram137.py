"""Print the value of key 'history' from the below dict
expected output 80
sampleDict={"class":{"student":{'name""Mike","mark":{"physics":70,"history":80}}}}"""
#sampleDict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
sampleDict = {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}

history_mark = sampleDict["class"]["student"]["marks"]["history"]
print(history_mark)  # Output: 80


