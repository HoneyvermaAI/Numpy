"""
      Indexing means returning the array or access the array or access the element at a particular index
      in an array.
      Syntax of indexing is--->
      array[indexNumber].
      negative index count the index from the last of the array.
"""
"""
       Slicing means extracting subarray for the parent or main array.
       Syntax of slicing is--->
       array[startingIndexNumber:EndingIndexNumber:steps]
       EndingIndexNumber is excluded means this index is not count in the print or calling..
       2nd method of slicing---->
       array[startingIndexNumber:EndingIndexNumber]
       In this Array we will goes till End - 1.
       if we pass -1 as steps it will reverse the array.
"""
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])

#print(arr[3])

print(arr[1:6])
print(arr[:6])
print(arr[1:6:2])
print(arr[::-1])
