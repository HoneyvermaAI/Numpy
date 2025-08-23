"""
      Fancying Means accessing more element at once using fancying.
      We use list in it to access all the particular element in the array or data.
      Syntax of fancying---->
      print(array[[indexOne, indexTwo, indexThree]]) we can add as much as index in it. Its depend on us.
      we pass nested list in it. [[   ]] like this.
"""
import numpy as np

array = np.array([10,20,30,40,50,60,70,80,90])
print(array[[0,2,5]])