#Write all content of a give file into a new file by skipping line number 5        # NO PROGRAM RUN

#read test file
with open ("D:\New folder\Given test.txt","r") as fp:
    #read all the lines from the file
    lines=fp.readlines()
#open new file in write mode
with open ("D:\New folder\new_file.txt","w") as fp:
    count=0
    #iterate each line from test file
    for line in lines:
        if count==4:
            count+=1
            continue
        else:
            fp.write(line)
        count+=1