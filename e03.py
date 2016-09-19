# e03
import numpy as np
import scipy.integrate

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)


'''
# Specify parameter
k = 1

# Specify my little time step
delta_t = 0.01

# Make an array of time points, evenly spaced up to 10
t = np.arange(0, 10, delta_t)

# Make an array to store the number of bacteria
n = np.empty_like(t)

# Set the initial number of bacteria
n[0] = 1

# Write a for loop to keep updating n as time goes on
for i in range(1, len(t)):
    n[i] = n[i-1] + delta_t * k * n[i-1]

plt.plot(t, n)
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of bacteria')

plt.show()
'''
# predator vs. prey PDEs #1
'''
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)
r = np.empty_like(t)
f = np.empty_like(t)
r[0] = 10
f[0] = 1

for i in range(1, len(t)):
        r[i] = r[i-1] + delta_t * (alpha * r[i-1] - beta * f[i-1] * r[i-1])
        f[i] = f[i-1] + delta_t * (delta * f[i-1] * r[i-1] - gamma * f[i-1])
    #r[i] = r[i-1] + delta_t * (alpha * r[i-1]-beta * f[i-1] * r[i-1])
    #f[i] = f[i-1] + delta_t * (delta * f[i-1] * r[i-1] - gamma * f[i-1])

plt.plot(t, r)
plt.plot(t,f)
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of prey/predator')
plt.legend(('prey', 'predator'), loc='upper right')
plt.show()
'''

'''
# Specify parameters
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)

# Make arrays to store rabbit and fox populations
r = np.empty_like(t)
f = np.empty_like(t)

# Set initial conditions
r[0] = 10
f[0] = 1

# Write a for loop to keep updating r and f as time goes on
for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * (alpha * r[i-1] - beta * f[i-1] * r[i-1])
    f[i] = f[i-1] + delta_t * (delta * f[i-1] * r[i-1] - gamma * f[i-1])

plt.plot(t, r)
plt.plot(t, f)
plt.xlabel('time (a.u.)')
plt.ylabel('population')
plt.legend(('rabbits', 'foxes'))
plt.show()
'''


# predator vs. prey PDEs #2
'''
def Lotka_Volterra(rf, t,alpha, beta, delta, gamma):
    """
    Right hand side for cascade X -> Y -> Z.  Return dy/dt and dz/dt.
    """
    # Unpack y and z
    r, f = rf

    # Compute dy/dt
    dr_dt = alpha * r-beta * f * r

    # Compute dz/dt
    df_dt = delta*f*r-gamma * f

    # Return the result as a NumPy array
    return np.array([dr_dt, df_dt])

# Parameters
alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001

# Time points we want for the solution
t = np.arange(0, 60, delta_t)

# Initial condition
rf_0=np.array([10.0,1.0])

# Package parameters into a tuple
args = (alpha, beta, delta, gamma)

# Integrate ODES
rf = scipy.integrate.odeint(Lotka_Volterra, rf_0, t, args=args)

print(rf.shape)
# Pluck out y and z
r, f = rf.transpose()
plt.plot(t, r)
plt.plot(t,f)
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number of prey/predator')
plt.legend(('prey', 'predator'), loc='upper right')
plt.show()
'''
# Generate sorted random numbers
x = np.sort(np.random.random(size=100000))

# Generate y-axis for CDF
y = np.arange(1, len(x)+1) / len(x)

# Plot CDF from random numbers (for plotting purposes, only plot 100 points)
plt.plot(x[::1000], y[::1000], marker='.', linestyle='none', markersize=10)

# Plot expected CDF (just a straight line from (0,0) to (1,1)
plt.plot([0, 1], [0, 1], 'k-')

def ecdf(data):
    """Compute x, y values for an empirical distribution function."""
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

# Compute ECDFs for 1975 and 2012
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
plt.plot(x_1975, y_1975, marker='.', linestyle='none')
plt.plot(x_2012, y_2012, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('beak depth (mm)')
plt.ylabel('ECDF')
plt.legend(('1975', '2012'), loc='lower right')
plot.show()
