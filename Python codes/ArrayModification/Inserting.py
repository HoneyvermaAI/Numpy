"""
    Inserting means Adding or change an element in an array.
    Syntax of Inserting--->
    np.insert(array , index , element, axis)
    axis = 0, means row wise.
    axis = 1, means column wise.
"""
import numpy as np

array = np.array([10,20,30,40,50,60,70,80,90])
array_inserting = np.insert(array,2, 100)
print(array_inserting)