#Assign  a different name to function and call it through the new name Below is the function display_student(name,age). Assign a new name 
#show_studnet(name,age) to it and call it using new name.
def display_student(name, age):
    print("name of student {} and his age is {}".format(name, age))

show_student = display_student
print(show_student("Mihir", 29))
