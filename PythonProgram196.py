""" Create a result array by adding the following two Numpy arrays. Next, modify the result array
by calculating the square of each element
arrayOne=numpy.array([[5,6,9],[21,18,27]])
array_Two=numpy.array([[15,33,24],[4,7,1]])"""
import numpy as np
arrayOne=np.array([[5,6,9],[21,18,27]])
arrayTwo=np.array([[15,33,24],[4,7,1]])
#print (arrayOne)
#print(arrayOne)
result_array=arrayOne+arrayTwo
print(result_array)
final_output=pow(result_array,2)
print(final_output)
                     