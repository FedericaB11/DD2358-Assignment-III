import ctypes
import numpy as np
from timeit import default_timer as timer
import os
import matplotlib.pyplot as plt

grid_shape = (256, 256)

_GaussSeidel = ctypes.CDLL("/home/federica/Documents/Courses/Intro_to_HPC/GaussSeidel.so")

# Create references to the C types 
TYPE_INT = ctypes.c_int
TYPE_DOUBLE = ctypes.c_double
TYPE_DOUBLE_SS = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

# Initialize the signature of the gauss_seidel function
_GaussSeidel.gauss_seidel.argtypes = [TYPE_DOUBLE_SS, TYPE_DOUBLE_SS]
_GaussSeidel.gauss_seidel.restype = None
def gauss_seidel(f, newf):
    # Convert the Python types into the C types
    assert np.shape(f) == (256, 256)
    pointer_f = f.ctypes.data_as(TYPE_DOUBLE_SS)  # numpy array
    pointer_newf = newf.ctypes.data_as(TYPE_DOUBLE_SS)  # numpy array

    # Call the function
    _GaussSeidel.gauss_seidel(pointer_f, pointer_newf)
    return newf
"""
N = grid_shape[0]
f = np.ones((N,N))
newf = np.zeros((N,N))
t1 = timer()
for k in range(1000):    
    newf = gauss_seidel(f, newf)
t2 = timer()
times = t2 -t1 
print(gauss_seidel.__name__ + " took", times, "seconds")
print(newf)
"""
N = grid_shape[0]
f = np.ones((N,N))
newf = np.zeros((N,N))
averages = []
stds = []
t = np.zeros((6,1))
for j in range(6):
    t1 = timer()
    for k in range(1000):    
        newf = gauss_seidel(f, newf)
    t2 = timer()
    t[j] = t2 - t1
    
averages.append(np.average(t))
stds.append(np.std(t))
print(averages)
print(stds)
 
N = [16, 32, 64, 128, 256]
av = [0.004708756333305549, 0.006214052166645463, 0.015069063000282767, 0.054901794666572336, 0.22209713383335838]
ax = plt.plot(N, av)
#plt.xticks(np.arange(0,5), ['50', '100', '200', '400', '800'])
plt.xlabel('Matrix size N')
plt.ylabel('Execution time (s)') 
plt.show()


