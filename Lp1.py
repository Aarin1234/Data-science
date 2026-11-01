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

#Specifying the data type during instatiation
float_array = np.array([1,2,3,4,5], dtype = 'i')
#if you want a float datatype exchange the 'i' with a 'f'
print(f'integer array : \n{float_array}\n')

#Creating a multi-dimensional array
twod_array = np.array([[1,2],[3,4]])
print('\ntwod array:')
print(twod_array, '\n')
'''When creating a multi-dimensional array,
all rows should have th same no. of Columns - otherwise Error'''

#Print the dimensions of the array
#ndim
print('the dimensions of the array:')
print(twod_array.ndim,'\n')

#Get an array of number from 1 - 20
num_array = np.arange(1, 20)
print('Get an array of numbers from 1 - 20\n', num_array), '\n'

#Get an array of numbers from 1-100 for even number only
even_array = np.arange(2, 101, 2)
print('Get an array of numbers from 1-100 for even numbers only')
print(even_array,'\n')

#Get a random arrangement of numbers
#Run again th get different arrangments
random_arr = np.random.permutation(np.arange(1,11))
print('Get a random arrange of arrangement of numbers')
print(random_arr,'\n')

#Get a random number using numpy
random_num = np.random.randint(1,10)
print('Get a random number using numpy')
print(random_num,'\n')

#Get the random numpy array specified dimension
random_array = np.random.rand(2,3)#row=2, col=3
print('Get the random numpy array of specified dimension (row=2, col=3):')
print('random_array')
print('shape = ',random_array.shape,'\n')
