#Stacking Along Columns
#NumPy provides a helper function: vstack()  to stack along columns.

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)