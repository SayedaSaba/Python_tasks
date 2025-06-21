'Create a 5 × 5 NumPy array of random integers (1 to 100). Replace all even numbers in the array with 0.'

import numpy as np

arr = np.random.randint(0,100,size= (5,5))
arr[arr%2==0]=0
print(arr)
