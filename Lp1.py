import numpy as np
sample_list = [1,2,3,4,5]
print(type(sample_list), '\n')

#Converting the list into an numpy array

sample_numpy_array = np.array(sample_list)
print(type(sample_numpy_array), '\n')

#Creating a numpy array of zeroes
zeros_array = np.zeros(5)
print(f'\n Zeros array : \n{zeros_array}\n')

#Creating a numpy array of ones
ones_array = np.ones(5)
print(f'\n Ones array : \n{ones_array}\n')
