import numpy as np

# Define the function
def f(t, y):
    return t - y**2

# Euler Method
def euler_method(f, t_range, y0, iterations):
    t0, tf = t_range
    h = (tf - t0) / iterations
    t = t0
    y = y0
    for _ in range(iterations):
        y += h * f(t, y)
        t += h
    return y

# Runge-Kutta Method (RK4)
def runge_kutta_method(f, t_range, y0, iterations):
    t0, tf = t_range
    h = (tf - t0) / iterations
    t = t0
    y = y0
    for _ in range(iterations):
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return y

# Parameters
t_range = (0, 2)
y0 = 1
iterations = 10

# Compute results
euler_result = euler_method(f, t_range, y0, iterations)
runge_kutta_result = runge_kutta_method(f, t_range, y0, iterations)

# Output results
print(f"Euler Method Result: {euler_result}")
print(f"Runge-Kutta Method Result: {runge_kutta_result}")
