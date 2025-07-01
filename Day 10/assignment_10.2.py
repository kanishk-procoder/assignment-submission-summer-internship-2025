#Move axes of 3D array to new positions
import numpy as np

arr = np.random.rand(2, 3, 4)
new_arr_transpose = np.transpose(arr)
print("1st type axis change : ", new_arr_transpose.shape)
new_arr_transpose = np.transpose(arr,(2,0,1))
print("2nd type axis change : ", new_arr_transpose.shape)
new_arr_transpose = np.transpose(arr,(1,2,0))
print("3rd type axis change : ", new_arr_transpose.shape)

