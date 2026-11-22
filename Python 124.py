import numpy as np
arr = np.linspace(0, 9, 10, dtype=int)
modified_arr = np.where(arr % 2 != 0, -1, arr)
reshaped_arr = arr.reshape(2, -1)
total_arr = arr.sum()

print("Original array:", arr)
print("Modified array:", modified_arr)
print("2D array:\n", reshaped_arr)
print("Sum of evens:", total_arr)
