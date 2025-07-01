#Study the following program
import numpy as np
# create a NumPy 1d-arrays
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
# Find average of NumPy arrays
avg = (arr1 + arr2) / 2
print("Average of NumPy arrays:\n", avg)
#Calculate average mean median mode values of two NumPy 2d-arrays

arr1 = np.array([[1, 2], [5, 4]])
arr2 = np.array([[6, 5], [7, 8]])
arr = np.stack((arr1,arr2))
avg = (arr1 + arr2) / 2
mean = np.mean([arr1, arr2])
median = np.median([arr1, arr2], axis=0)
values, count = np.unique(arr.flatten(), return_counts=True)
mode = values[np.argmax(count)]
print("\nAverage : ", avg)
print("\nMean : ", mean)
print("\nMedian : ", median)
print("\nMode : ", mode)