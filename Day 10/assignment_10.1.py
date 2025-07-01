#Replace Nan with 0 and Interchange 3 rows and 3 columns of 2D array [[6, -8, 73, -110], [np.nan, -8, 0, 94]]
import numpy as np

arr = np.array([[6,-8,73,-110], [np.nan,-8,0,94]])
arr = np.nan_to_num(arr, nan=0)
arr[:,[0,1,2]] = arr[:,[1,2,0]]
print(arr)