"""
    Concatenate means Adding two or more arrays together.
    syntax--->
    np.concatenate((array1,array2) , axis = 0)
    axis = 0 means store data as row wise.
    axis = 1 means store data as column wise.
"""
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr = np.concatenate((arr1,arr2) , axis=0)
print(new_arr)