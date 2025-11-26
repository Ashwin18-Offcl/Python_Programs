""" Sort by the folloeing NumPy array
Case 1: Sort by the second row
Case 2: Sort array by the second column"""
""" sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])"""
import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

#sorting original array by second row

sortArrayByRow = sampleArray[sampleArray[1,:].argsort()]
print(sortArrayByRow)
sortArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
print(sortArrayByColumn)
