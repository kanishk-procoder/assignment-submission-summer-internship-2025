import numpy as np
# combining a one and 2d array numpy array
arr_1d = np.arange(10,13)
arr_2d = np.arange(9).reshape(3,3)

print(arr_1d)
print("\n")
print(arr_2d)
print("\n")

res_arr = np.vstack((arr_2d, arr_1d))
print("concatenated array : ")
print(res_arr)
print("\n")

#flatten a 2d array into a 1d array.
res_arr = res_arr.flatten()
print(res_arr)
print("\n")

#Reverse a numpy array
arr = np.arange(10).reshape(2,5)
rev_arr = np.flip(arr)
print(rev_arr)
print("\n")

#Practice operations like
#       Get the maximum value from given array
#       Get the minimum value from given array
#       Find the number of rows and columns of a given array using NumPy
#       Select the elements from a given array (each element and specific element)
#       Find the sum of values in a 2D array using for loop
#       Adding, Subtracting, multiplying, dividing arrays in Numpy

arr = np.array([2,7,5,9,0,22,96,97,45,76,69,80]).reshape(4,3)
print(arr)
print("\n")
print(arr.max())
print("\n")
print(arr.min())
print("\n")
print(arr.shape)
print("\n")
print("printing each element : ")
for i in np.nditer(arr):
    print(i)
print("printing specific element : ")
print(arr[1,2])
print("\n")
total = 0
for rows in arr:
    for i in rows:
        total += i
print(total)

arr1 = np.array([19,29,37,5,2,52,25,14]).reshape(4,2)
arr2 = np.array([78,63,33,98,78,48,61,74]).reshape(4,2)

print("\nsum : ")
print(arr1 + arr2)
print("\nsubtracting : ")
print(arr1 - arr2)
print("\nmultiplication : ")
print(arr1 * arr2)
print("\ndivision : ")
print(arr1 / arr2)