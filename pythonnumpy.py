# pip install numpy

import numpy as np

# 1D array

# arr1d = np.array([10,20,30,410,50])
# print(arr1d)
# print(arr1d[0])
# arr2d = np.array([[10,20,30],[40,50,60]]) 

# # print(arr2d[0:2])
# print(arr2d[:2,2]) #0,1

# arr3d = np.array([[10,20,30],[40,50,60],[500,600,700]]) 
# print(arr3d[arr3d>20])

# ze = np.zeros((3,4))
# print(ze)
# one =  np.ones((3,4))
# print(one)

# eye = np.eye(3)
# print(eye)

# arrays = np.arange(0,10,2)
# print(arrays)

# rands = np.random.randint(4000)
# print(rands)

# lineSpace = np.linspace(0,1,5)
# print(lineSpace)

# arr1 = np.array([10,20,30])
# print(np.min(arr1))

arr = np.arange(12)
print(arr)

mats = arr.reshape(3,4)
print(mats)

flat = mats.flatten()
print(flat)