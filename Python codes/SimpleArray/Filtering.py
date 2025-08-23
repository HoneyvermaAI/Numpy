"""
     Filter or boolean masking is used to apply filters like less than or greater than or equals and many
     more.
     Syntax of filtering is--->
     print(array[array > 25])
     It is  faster than loops
"""
import numpy as np

array = np.array([10,20,30,40,50,60,70,80,90])
print(array[array < 60])