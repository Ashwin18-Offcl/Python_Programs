#Pyramid Structure/ generate the pascal triangle
n = int(input("Enter the number: "))
list1 = []

# Generating Pascal's Triangle
for i in range(n):
    temp = []
    for j in range(i + 1):
        if j == 0 or j == i:
            temp.append(1)
        else:
            temp.append(list1[i - 1][j - 1] + list1[i - 1][j])
    list1.append(temp)

# Printing Pascal's Triangle
for i in range(n):
    # Print leading spaces
    for j in range(n - i - 1):
        print(" ", end="")
    # Print numbers in the row
    for j in range(i + 1):
        print(list1[i][j], end=" ")
    print()
