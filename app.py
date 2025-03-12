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
    v1,v2,v3 = Y # vi =y v2 = dy/dt v3 = d^2y/dt^2
    dv1_dt = v2
    dv2_dt = v3
    dv3_dt = -4*v3 - 5*v2 -2*v1
    return [dv1_dt, dv2_dt, dv3_dt]

initial_conditions = [1,0,0]
t_span = (0,10)
t_eval = np.linspace(0,10,100)

sol = solve_ivp(sys,t_span, initial_conditions, t_eval=t_eval)


plt.plot(sol.t, sol.y[0], label="y(t) (position)")
plt.plot(sol.t, sol.y[1], label="v(t) (velocity)", linestyle="dashed")
plt.plot(sol.t, sol.y[2], label="d²y/dt² (acceleration)", linestyle="dotted")
plt.xlabel("t")
plt.ylabel("solution")
plt.legend()
plt.grid()
plt.title("Solution to 3nd ode converted to 1st order system")
plt.show()