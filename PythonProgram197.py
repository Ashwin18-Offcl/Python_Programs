""" Split the array into four equal-sized sub-arrays
Note; create 8X3 inter array from a range between 10 to range between 10 to 34 such that the difference between each
element is 1 and then Split the array into four euqal-sized sub-arrays."""
import numpy as np

new_array=np.arange(10,34,1)
new_array=new_array.reshape(8,3)
print(new_array)
#NOW TO DIVIDE ARRAY INTO 4 EQUAL DIVISION
subarray=np.split(new_array,4)
print("="*100)
print(subarray)
