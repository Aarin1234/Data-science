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
#Shape gives the numbers of rows and columns in an array
#Reshape a linear array to required dimension
reshaped_array = np.arange(1,10).reshape(3,3)
print(f'Reshaped array = \n {reshaped_array}\n')
print(f'Reshaped arr shape = {reshaped_array.shape}\n')

linear_array = np.arange(1,37)
print(f'Here is 1 - 36: {linear_array}\n')

reshape1 = linear_array.reshape(6,6)
print(f'Linear array with 6 rows and 6 columns: \n{reshape1}\n')

reshape2 = linear_array.reshape(9,4)
print(f'Linear array with 9 rows and 4 columns: {reshape2}\n')

reshape3 = linear_array.reshape(3,12)
print(f'Linear array with 3 rows and 12 columns: {reshape3}\n')
#The total number of items should remain the same after reshaping

random_array = np.random.permutation(np.arange(1,10))
print(f'Random array: {random_array}\n')
sorted_array = np.sort(random_array)
print(f'Sorted array: {sorted_array}')

#Create an array containing 4 numbers between 1 to 25
array4num = np.linspace(1,25,4)
print(f'{array4num}')
'''Linspace(): this function creates an array cotaining a fixed
number of items between two specific numbers such that the 
differnce between any two consecutive numbers in the array is 
constant, we give the third number as the total number of items
into the array.

arange() it returns one dimensional array containing two specified 
numbers, such that the difference between a pair of two constant
numbers in the arry.
here we provide the third number as the difference between to
consecutive numbers'''


'''Create an array containing 10 numbers between 1 to 25 such that 
the difference between two consecutive numbers is constant'''
numbers = np.linspace(1,25, 10)
print(f'\n10 numbers between 1 to 25: {numbers}')
