import numpy as np 
cimport numpy as np


def copy_s(double[:] a, double[:] c):
    cdef unsigned int j
    for j in range(len(a)):
        c[j] = int(a[j])
    return c

def scale_s(double[:] b, double[:] c, int scalar):
    cdef unsigned int j
    for j in range(len(b)):
        b[j] = scalar*c[j]
    return b
    
def sum_s(double[:] a, double[:] b, double[:] c):
    cdef unsigned int j
    for j in range(len(a)):
        c[j] = a[j]+b[j]
    return c
    
def triad_s(double[:] a, double[:] b, double[:] c, int scalar):
    cdef unsigned int j
    for j in range(len(a)):
        a[j] = b[j]+scalar*c[j]
    return a