import numpy as np

SMAX = np.ones((10,10))
for i in range(10):
    for j in range(10):

        shift =np.min([(i - j),(i+j)])
        SMAX[i,j] = shift

time = np.linspace(0,20,200000)

Iext = np.zeros((10, 1)) #external current
for t in range(10):
    check = (time[t] >= 0 and time[t] <= 5)#  and  (x >= -2.5 and x <=  2.5)
    Iext[t] = 5 if check else 0
print(Iext)

