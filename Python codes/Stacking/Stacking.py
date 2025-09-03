"""
   Stacking means arranging the array or data horizontally and vertically.
   Syntax---->
   np.vstack((array1, array2)) vstack is used to stack array as row wise or vertically.
   np.hstack((array1, array2)) hstack is used to stack array as column wise or horizontally.
"""

import numpy as np
from numpy.ma.extras import vstack

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_array1 = np.vstack((arr1,arr2))
new_array2 = np.hstack((arr1,arr2))
print("Stacking Row wise or vertically",new_array1)
print("Stacking column wise or horizontally",new_array2)