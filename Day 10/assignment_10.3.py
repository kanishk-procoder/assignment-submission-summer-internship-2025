#Replace NaN values with average of columns
import numpy as np
arr = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
col_means = np.mean(np.nan_to_num(arr,True,0), axis=0)
arr = np.nan_to_num(arr,True,col_means)
print(arr)
