import numpy as np

empty_array = np.empty((0, 4), int)
print('Empty 2D Numpy array:')
print(empty_array.shape)

# Append a row to the 2D numpy array
empty_array = np.append(empty_array, np.array([[11, 21, 31, 41]]), axis=0)
# Append 2nd rows to the 2D Numpy array
empty_array = np.append(empty_array, np.array([[15, 25, 35, 45]]), axis=0)
print('2D Numpy array:')
print(empty_array)