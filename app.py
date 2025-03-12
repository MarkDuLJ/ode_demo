import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

'''
# define ode func
let v = dy/dt
2nd order ode convert to 1st order
initial conditions: y(0) = 1, dy/dt(v) at t=0 is 0
'''
def sys(t,Y):
    y,v = Y # y = position, v = velocity
    dydt = v
    dvdt = -3*v -2*y
    return [dydt, dvdt]

y0 = [1,5]
t_span = (0,10)
t_eval = np.linspace(0, 10,100)

sol = solve_ivp(sys,t_span, y0, t_eval=t_eval)

plt.plot(sol.t, sol.y[0], label="y(t) (position)")
plt.plot(sol.t, sol.y[1], label="v(t) (velocity)", linestyle="dashed")
plt.xlabel("t")
plt.ylabel("solution")
plt.legend()
plt.grid()
plt.title("Solution to 2nd ode converted to 1st order system")
plt.show()