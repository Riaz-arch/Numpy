import numpy as np

original_array = np.linspace(0, 9, num=10) 
print("Original Array:", original_array)

modified_array = np.where(original_array % 2 != 0, -1, original_array)
print("Modified Array (odd numbers replaced with -1):", modified_array)

new_2d_array = modified_array.reshape(2, -1)  
print("2D Array with two rows:\n", new_2d_array)

sum_of_evens = np.sum(original_array[original_array % 2 == 0])
print("Sum of all even numbers in the original array:", sum_of_evens)