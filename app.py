import numpy as np
import matplotlib.pyplot as plt

# Global Parameters
N = 1000
kappa = 15*np.sqrt(2)

# Spatial Domain Discretization
L = 40
nx = N
dx = L/nx
x = np.linspace(-L/2, L/2, nx)

# Time Domain Discretization
tend = 20
dt = 10 ** (-4)
nt = int(np.round(tend/dt))
time = np.linspace(0,tend,nt) #time has 200,000 elements

# Lorentzian??? distribution of the background current
eta0 = -10  #center
hw = 2      #half width
eta = np.zeros((N, 1)) #  N×1 array with zero value

# loop give eta value
for j in range(0,N):
    eta[j] = eta0 + hw*np.tan((np.pi/2)*((2*j-N-1)/(N+1))) #TODO:confirm the formular


# Spatial Coupling Kij
def K(x):
    return np.exp(-np.abs(x)) - .25*np.exp(-np.abs(x)/2)

SMAX = np.ones((N,N)) # N x N matrix filled with ones
for i in range(N):
    for j in range(N):
        shift = np.min([np.abs(i-j),N - np.abs(i-j)] )
        SMAX[i,j] = K(shift*dx)


# Store firing information
vpeak = 200
vreset = -vpeak

'''
[[0. 0.]
 [0. 0.]
 [0. 0.]
 ...
 [0. 0.]
 [0. 0.]
 [0. 0.]]
'''
firings = np.zeros((N*nt, 2))
ns = 0

# Initialize
v = np.zeros((N, 1))
vt = np.zeros((N, nt))

Isyn = np.zeros((N, 1)) #synaptic current
Iext = np.zeros((N, 1)) #external current

tspike = np.zeros((N, nt))

# Time Evolution
for t in range(nt):
    Iext = 5 * ((x >= -2.5) & (x <= 2.5) & (time[t] >= 0) & (time[t] <= 5))

    # Update states using Euler method
    dv = v**2 + eta + Iext + kappa*Isyn
    v = v + dt*dv
    
print(Iext)

'''
plt.plot(range(N), eta, marker='o',label='demo')
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("distribution")
plt.legend()
plt.grid(True)
plt.show()
 '''