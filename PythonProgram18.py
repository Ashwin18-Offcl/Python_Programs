#Check file is empty or not Write a program to check if the given file is empty or not
#program Error Shows You Not entered this program file location copy and just paste
import os
size=os.stat("E:\PYTHON PROJECTS\PythonProgram18.py").st_size

if size==0:
    print("file is empty")
else:
    print("file is not empty")
