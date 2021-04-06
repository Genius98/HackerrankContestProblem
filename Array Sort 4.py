#Write a NumPy program to sort the specified number of elements from beginning of a given array

import numpy as np
nums =  np.random.rand(10)
print("Original array:")
print(nums)
print("\nSorted first 5 elements:")
print(nums[np.argpartition(nums,range(5))])
