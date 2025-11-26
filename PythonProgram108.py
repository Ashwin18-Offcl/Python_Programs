#Extract the email servivce provider name
emaillist=["KSR@datavizion.com","mymail@yahoo.com","milindmali@google.com","snehal@healthcare"]
for i in emaillist:
    i=i.replace("@",".").split(".")
    print(i[1])

