import ctypes
import numpy as np
from timeit import default_timer as timer
from ctypes import *
import os

grid_shape = (800, 800)

_GameLife = ctypes.CDLL("/home/federica/Documents/Courses/Intro_to_HPC/GameLife.so")

# Create references to the C types 
TYPE_INT = ctypes.c_int
TYPE_DOUBLE = ctypes.c_double
TYPE_DOUBLE_SS = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
TYPE_INT_SS = ctypes.POINTER(ctypes.POINTER(ctypes.c_int))

# Initialize the signature of the update function 
_GameLife.update.argtypes = [TYPE_INT_SS, TYPE_INT_SS, TYPE_INT]
_GameLife.update.restype = None

def update(grid, newGrid, N):
    
    assert np.shape(grid) == (800, 800)
    cN = TYPE_INT(N)
    pointer_grid = grid.ctypes.data_as(TYPE_INT_SS)  # numpy array
    pointer_newGrid = newGrid.ctypes.data_as(TYPE_INT_SS)  # numpy array
    
    # Call the function
    _GameLife.update(pointer_grid, pointer_newGrid, cN)
    return newGrid

# Python code to implement Conway's Game Of Life
import argparse
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from timeit import default_timer as timer

 
# setting up the values for the grid
ON = 255
OFF = 0
vals = [ON, OFF]
 
def randomGrid(N):
 
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)
 
def addGlider(i, j, grid):
 
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,    0, 255],
                       [255,  0, 255],
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider
 
def addGosperGliderGun(i, j, grid):
 
    """adds a Gosper Glider Gun with top left
       cell at (i, j)"""
    gun = np.zeros(11*38).reshape(11, 38)
 
    gun[5][1] = gun[5][2] = 255
    gun[6][1] = gun[6][2] = 255
 
    gun[3][13] = gun[3][14] = 255
    gun[4][12] = gun[4][16] = 255
    gun[5][11] = gun[5][17] = 255
    gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 255
    gun[7][11] = gun[7][17] = 255
    gun[8][12] = gun[8][16] = 255
    gun[9][13] = gun[9][14] = 255
 
    gun[1][25] = 255
    gun[2][23] = gun[2][25] = 255
    gun[3][21] = gun[3][22] = 255
    gun[4][21] = gun[4][22] = 255
    gun[5][21] = gun[5][22] = 255
    gun[6][23] = gun[6][25] = 255
    gun[7][25] = 255
 
    gun[3][35] = gun[3][36] = 255
    gun[4][35] = gun[4][36] = 255
 
    grid[i:i+11, j:j+38] = gun

#removed img as second input argument and output

# main() function
#@profile
def main():
 
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.")
 
    # add arguments
    parser.add_argument('--grid-size', dest='N', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()
     
    # set grid size
    N = 800
    if args.N and int(args.N) > 8:
        N = int(args.N)

    # set animation update interval
    updateInterval = 50
    if args.interval:
        updateInterval = int(args.interval)
 
    # declare grid
    grid = np.array([])
 
    # check if "glider" demo flag is specified
    if args.glider:
        grid = np.zeros(N*N).reshape(N, N)
        addGlider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(N*N).reshape(N, N)
        addGosperGliderGun(10, 10, grid)
 
    else:   # populate grid with random on/off -
            # more off than on
        grid = randomGrid(N)
    
    #fig, ax = plt.subplots()
    #img = ax.imshow(grid, interpolation='nearest')
    num_iterations = 100
    N = 800
    ON = 255
    OFF = 0 
    newGrid = grid.copy()
    time1 = timer()
    for i in range(num_iterations):
        newGrid = update(grid, newGrid, N)
    time2 = timer()
    totalt= time2 - time1
    print(update.__name__ + " took", totalt, "seconds")
    return newGrid


# call main
"""
if __name__ == '__main__':
    print(main())
"""

# Average times and standard deviations for different grid sizes 
N = 800
averages = []
stds = []
t = np.zeros((6,1))
for j in range(6):
    t1 = timer()
    if __name__ == '__main__':
        main()
    t2 = timer()
    t[j] = t2 - t1
    
averages.append(np.average(t))
stds.append(np.std(t))
        
print(averages)
print(stds)

N = [50, 100, 200, 400, 800]
av = [0.0016851304923572268, 0.004598299502201068, 0.01601616149370481, 0.06262825100323728, 0.23946594816758685]
ax = plt.plot(N, av)
#plt.xticks(np.arange(0,5), ['50', '100', '200', '400', '800'])
plt.xlabel('Matrix size N')
plt.ylabel('Execution time (s)') 
plt.show()
