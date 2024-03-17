import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1/7)*x**7 - x**3 + (1/2)*x**2 - x

x_values = np.linspace(0.5, 1.5, 400)
x_values_extended = np.linspace(0.3, 1.7, 1000) 
y_values = f(x_values)
y_values_extended = f(x_values_extended)

min_point_x = x_values[np.argmin(y_values)]
min_point_y = min(y_values)

plt.plot(x_values, y_values, label='$f(x) = \\frac{1}{7}x^7 - x^3 + \\frac{1}{2}x^2 - x$', color='blue')
plt.scatter(min_point_x, min_point_y, color='red', label=f'Minimum at ({min_point_x:.2f}, {min_point_y:.2f})')
plt.plot(x_values_extended, y_values_extended, linestyle='--', color='gray')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции $f(x) = \\frac{1}{7}x^7 - x^3 + \\frac{1}{2}x^2 - x$')
plt.legend()
plt.grid(True)
plt.show()
