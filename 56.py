#NumPy Joining Array
#Joining NumPy Arrays
#Joining means putting contents of two or more arrays in a single array.
# concatenate() function

#Join two arrays ?

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)