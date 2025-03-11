import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# define ode func dy/dt = -2y
def dydt(t,y):
    return -2 * y

# initial condition y(0) = 1
y0 = [1]

# time span from t=0 to t=5
t_span = (0,5)

# solve the ode
sol = solve_ivp(dydt,t_span, y0, t_eval=np.linspace(0,5,10))

# plot the solution
plt.plot(sol.t, sol.y[0], label=r"$\frac{dy}{dt} = -2y$")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()
plt.grid()
plt.show()