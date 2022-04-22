#cythonfngauss
def gauss_seidel(double[:,:] f):
    cdef unsigned int i, j
    cdef double[:,:] newf = f.copy()
    cdef unsigned int rows = newf.shape[0]
    cdef unsigned int cols = newf.shape[1]
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            newf[i,j] = 0.25  * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])
    return newf