import time
from timeit import default_timer as timer
import sys
from array import *
import numpy as np
import matplotlib.pyplot as plt
import cythonfnstream

# List


STREAM_ARRAY_SIZE = []
for i in range(100):
    STREAM_ARRAY_SIZE.append(i**2)

bandwidth_copy = []
bandwidth_scale = []
bandwidth_sum = []
bandwidth_triad = []
times_bandwidth = []

    
def copy_s(a, c):
    for j in range(len(a)):
        c[j] = int(a[j])
    return c

def scale_s(b, c, scalar):
    for j in range(len(b)):
        b[j] = scalar*c[j]
    return b

def sum_s(a, b, c):
    for j in range(len(a)):
        c[j] = a[j]+b[j]
    return c

def triad_s(a, b, c, scalar):
    for j in range(len(a)):
        a[j] = b[j]+scalar*c[j]
    return a

for i in STREAM_ARRAY_SIZE:

    a = array('d', range(i))
    b = array('d', range(i))
    c = array('d', range(i))
    times = list(range(4))
    
    for j in range(i):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0
    scalar = 2.0

    # copy
    times[0] = timer()
    c_copy = cythonfnstream.copy_s(a, c)
    times[0] = timer() - times[0]
    print(copy_s.__name__ + " took", times[0], "seconds")

    # scale
    times[1] = timer()
    b = cythonfnstream.scale_s(b, c, scalar)
    times[1] = timer() - times[1]
    print(scale_s.__name__ + " took", times[1], "seconds")
    
    #sum
    times[2] = timer()
    b_sum = cythonfnstream.sum_s(a, b, c)
    times[2] = timer() - times[2]
    print(sum_s.__name__ + " took", times[2], "seconds")

    # triad
    times[3] = timer()
    a = cythonfnstream.triad_s(a, b,c,  scalar)
    times[3] = timer() - times[3]
    print(triad_s.__name__ + " took", times[3], "seconds")
    
    bandwidth_copy.append((2 * sys.getsizeof(a) * i)/times[0])
    bandwidth_sum.append((2 * sys.getsizeof(a) * i)/times[1])
    bandwidth_scale.append((3 * sys.getsizeof(a) * i)/times[2])
    bandwidth_triad.append((3 * sys.getsizeof(a) * i)/times[3])
    times_bandwidth.append((times))
    
print(times_bandwidth)
#print(bandwidth_copy)
#print(bandwidth_sum)
#print(bandwidth_scale)
#print(bandwidth_triad)

# Plot results
plt.plot(STREAM_ARRAY_SIZE, bandwidth_copy, 'darkorange')
plt.plot(STREAM_ARRAY_SIZE, bandwidth_sum, 'deepskyblue')
plt.plot(STREAM_ARRAY_SIZE, bandwidth_scale, 'blue')
plt.plot(STREAM_ARRAY_SIZE, bandwidth_triad, 'deeppink')
plt.xlabel('STREAM_ARRAY_SIZE')
plt.ylabel('Bandwidth')
plt.legend(['Copy', 'Sum', 'Scale', 'Triad'])
plt.show()