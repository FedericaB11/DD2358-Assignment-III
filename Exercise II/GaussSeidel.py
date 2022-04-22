import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt 

#Gauss Seidel function

#@profile
def gauss_seidel(f):
    newf = f.copy()
    
    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = 0.25 * (newf[i,j+1] + f[i,j-1] +
                                   newf[i+1,j] + f[i-1,j])
    return newf

# Call function for specific N

N = 100
f = np.ones((N,N))
t1 = timer()
for k in range(10):    
    newf = gauss_seidel(f)
    print(newf)
t2 = timer()
times = t2 -t1 
print(gauss_seidel.__name__ + " took", times, "seconds")

# Average times and standard deviations for different grid sizes and results plot
"""
averages = []
stds = []
N = [16, 32, 64, 128, 256]
t = np.zeros((len(N),6))
for j in range(6):
    for i in range(len(N)):
        f = np.ones((N[i],N[i]))
        t1 = timer()
        for k in range(1000):    
            newf = gauss_seidel(f)
        t2 = timer()
        t[i,j] = t2 - t1
averages.append(np.average(t, axis=1))
stds.append(np.std(t, axis=1))
        
print(averages)
print(stds)

# Plot of the results
ax = plt.plot(N, list(averages[0]))
#plt.xticks(np.arange(0,8), ['8', '16', '32', '64', '128', '256','512','1024'])
plt.xlabel('Matrix size N')
plt.ylabel('Execution time (s)')
"""
