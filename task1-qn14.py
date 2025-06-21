'Create two 3×3 NumPy arrays with random integers. Write code to check and return a boolean array showing element-wise equality.'


import numpy as np

arr1 = np.random.randint(1,11,size=(3,3))
arr2 = np.random.randint(1,11,size=(3,3))

comparison_result = arr1 == arr2

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)
print("Element-wise Equality:\n", comparison_result)