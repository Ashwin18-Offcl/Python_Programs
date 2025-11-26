""" Access the nested key 'salary' from the following JSON """
import json
sampleJson = """
{
"company":{
"emplopee":{
"name":"emma",
"payble":{
"salary":7000,
"bonus":800
}
}
}
}
}"""
#write code to print the value of salary
data=json.loads(sampleJson)
print(data["company"]["emplpyee"]["payble"]["salary"])
