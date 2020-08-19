### introduction
#numpy helps to perform operations on arrays and matrices


### Import
import numpy as np
print ("NumPy version - " + np.version.version)

### Create Arrays

#basic array
array_1d = np.array([10, 11, 12, 13])
print (array_1d)
#array from a list
list_1 = [11, 22, 33, 44, 55]
array_l1 = np.array(list_1)
print(array_l1)

#check shape of array
print(array_1d.shape)
#check type of array
type(array_1d)

#range of values
#last number is exclusive
plain_range = range(1,50)
list(plain_range)
interval_range = range(1, 10, 3)
list(interval_range)


### Create 2-D Arrays

#basic matrix
mymatrix = [list(range(1,10,1)),list(range(11,20,1))]
mymatrix
numpy_array = np.array(mymatrix)
numpy_array
type(numpy_array)


### Convert NumPy array to a Pandas Frame
import pandas as pd
df_from_array = pd.DataFrame(numpy_array)
df_from_array


### Indexing and Slicing

#create 1D array
array_1d = np.array([6,4,4,4,4,5,5,5,5])
print (array_1d)
#remember that python starts at 0
print('element at index1:', array_1d[0])
#arrays are mutable, so change element at index 1
array_1d[0] = 7
print('element at index1:', array_1d[0])
print (array_1d)
print('elements in the range:', array_1d[1:7])

#create 2D array
array_2d = np.array([[11, 12, 13, 14, 15, 16, 17], [21, 22, 23, 24, 25, 26, 27], [31, 32, 33, 34, 35, 36, 37]])
print ('original array: \n', array_2d, '\n')
#slicing: generates an array of the same rank
array_copy = array_2d.copy()
slice_row = array_copy[1:2, :] #a:b - including a, until (and excluding) b
print ('sliced array on [1:2, :]: \n', slice_row)

### Arithmetic on Arrays

