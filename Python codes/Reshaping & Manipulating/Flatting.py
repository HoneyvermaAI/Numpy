"""
    When we to covert MultiDimensional array into 1D array. we use flatten() and ravel().
    .Ravel() it returns view and may affect the array.
    .Flatten() it returns copy and do not affect the array.
"""
import numpy as np
array_2d = np.array([[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18]])
print(array_2d.ravel())
print(array_2d.flatten())