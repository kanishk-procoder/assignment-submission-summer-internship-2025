import numpy as np

# Create a Numpy array
#       with random values
#       (4x2) empty and a full NumPy array
#       (3x5) array filled with all zeros
#       (4x3x2) array filled with all ones

rand_arr = np.random.rand(5)
print(rand_arr)
print("\n")

empty_arr = np.empty((4,2))
print(empty_arr)
print("\n")

full_arr = np.full((4,2),fill_value="*")
print(full_arr)
print("\n")

zero_arr = np.zeros((3,5))
print(zero_arr)
print("\n")

ones_arr = np.ones((4,3,2))
print((ones_arr))
print("\n")

# Write a NumPy program to create a 3x3 2D matrix with values ranging from 2 to 10.

arr = np.arange(2,11).reshape(3,3)
print(arr)
print("\n")

# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.

null_arr = np.zeros(10)
null_arr[5] = 11
print(null_arr)
print("\n")

# Write a NumPy program to reverse an array (the first element becomes the last).

arr = np.arange(10)
print(arr)
print(arr[::-1])
print("\n")

# Write a NumPy program to convert an array to a floating type.

arr = np.array([1, 2, 3, 4])
print("array before dtype change : \n",arr)
arr = np.float64(arr)
print("array before dtype change : \n",arr)