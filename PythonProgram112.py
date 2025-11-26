#Slice list into 3 equal chunks and reverse each chunk
sample_list = [11,49,8,23,14,12,78,45,89]

n=int(len(sample_list)/3)

l1=sample_list[0:n]
l2=sample_list[n:n*2]
l3=sample_list[n*2:n*3]

print("chunk 1",l1)
print("Reversed of chunk 1",l1[::-1])

print("Chunk 2",l2)
print("Reversed of chunk 3",l2[::-1])

print("chunk 3",l3)
print("Reversed of chunk 3",l3[::-1])
