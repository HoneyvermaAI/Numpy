"""
     Reshaping means changing the dimensions or shape without change the actual data or modifying the actual
     data.
     Dimensions should match.
     Syntax of the reshape is--->
     array.reshape(rows , column)
"""
import numpy as np
from numpy.ma.core import reshape

array = np.array([1,2,3,4,5,6])
reshape_array = array.reshape(2,3)
print(reshape_array)
