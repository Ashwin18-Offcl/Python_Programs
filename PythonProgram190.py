"""Create a 4X2 integer array and prints its attributes
Note: The element must be a type of unsigned int 16. And print the following Attributes:-
the shape of an array
Array dimentions.
The Length of each element of the array in butes.
"""
import numpy as np
firstArray = np.empty([4,2],dtype = np.uint16)
print(firstArray)
print("shape of the array is:",firstArray.shape)
print("dimention of the array is:",firstArray.ndim)
print("itemsize of each element in array is:",firstArray.itemsize)