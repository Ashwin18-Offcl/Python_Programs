""" Print max from axix 0 and min from axix 1 from the following 2-D array
sampleArray=numpy.array([[34,43,73],[82,22,12],[53,94,66]])"""
import numpy
print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)
minOfAxixone = numpy.amin(sampleArray,1)
print("Printing amin Of Axis 1")

maxOfAxixOne = numpy.amax(sampleArray,0)
print("Printing amax Of Axis 0")
print(maxOfAxixOne)