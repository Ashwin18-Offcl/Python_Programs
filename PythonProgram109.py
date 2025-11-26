#Extract all the emailid for the given string
string = "H1 my name is Govind Das and my mail id is milindmali08@gmail.com and my org mail milind@google.com"
new = list(string.split())
for i in new:
    if ".com" in i:
        print(i)
