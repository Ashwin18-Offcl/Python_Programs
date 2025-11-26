#Create a fuction with a default argument Write a program to create a function
#show_mployee()using the following conditions.
#It Should accept the employee's name and salary and display  and both. if the salary is missing int the fuction call then assign default value 9000 to salary
def show_employee(name,salary="9000"):
    print("name of employee is {} and his\her salary is {}".format(name,salary))

print(show_employee("milid",78686))

print(show_employee("vishal"))
