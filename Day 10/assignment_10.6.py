#Solve the following equation using linalg() and inverse Matrix method:
#       x - 2y + 3z = 9
#       -x + 3y - z = -6
#       2x - 5y + 5z = 17

import numpy as np

arr1 = [[1,-2,3],[-1,3,-1],[2,-5,5]]
arr2 = [9,-6,17]
res = np.linalg.solve(arr1,arr2)
print(res)

arr3 = np.linalg.inv(arr1)
res = np.dot(arr3,arr2)
print(res)