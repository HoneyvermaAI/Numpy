import numpy as np
from scipy.sparse import eye_array

# This is for the 1d array
arr1d = np.array([1,2,3,4,5,6,7,8,9])
print("This is 1D array ",arr1d)

# for 2d array or for matrix

arr2d = np.array([[1,2,3,4],
                    [5,6,7,8],
                  [8,9,10,11]])
print("This is 2D array ",arr2d)

# if we want to fill our array with zeros and want to replace when the values will present in future

zeros = np.zeros(3)
print("This is for the zeros " ,zeros)

# if we want to fill our array with ones and want to replace when the values will present in future

ones = np.ones((2,3))
print("This is for the ones ",ones)

# if we want to fill our array with a specific value
# syntax np.full((shape) , value)
specific_val = np.full((2,3),4)
print("This is for the specific value ",specific_val)

# if we want to create identity matrix like ones in the digonal and rest is zeros
# syntax np.eye(shape)

identity_matrix = np.eye(3)
print("This is for the identity matrix ", identity_matrix)