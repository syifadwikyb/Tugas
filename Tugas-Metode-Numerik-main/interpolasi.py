import numpy as np
import matplotlib.pyplot as plt

# Interpolasi menggunakan metode polinom Lagrange
def lagrange_interpolation(x_data, y_data, x):
    n = len(x_data)
    result = 0.0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result

# Interpolasi menggunakan metode polinom Newton
def newton_interpolation(x_data, y_data, x):
    n = len(x_data)
    coefficients = np.zeros(n)
    for i in range(n):
        coefficients[i] = y_data[i]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i-1]) / (x_data[i] - x_data[i-j])
    result = 0.0
    for i in range(n):
        term = coefficients[i]
        for j in range(i):
            term *= (x - x_data[j])
        result += term
    return result

# Membuat Polinom Lagrange dari data
def lagrange_polynomial(x_data, y_data):
    n = len(x_data)
    polynomial = ''
    for i in range(n):
        term = f'{y_data[i]:.2f}'
        for j in range(n):
            if j != i:
                term += f' * (x - {x_data[j]}) / ({x_data[i]} - {x_data[j]})'
        polynomial += term
        if i != n - 1:
            polynomial += ' + '
    return polynomial

# Data yang diberikan
x_data = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_data = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Titik-titik untuk plotting grafik hasil interpolasi
x_values = np.linspace(5, 40, 500)
y_lagrange = [lagrange_interpolation(x_data, y_data, x) for x in x_values]
y_newton = [newton_interpolation(x_data, y_data, x) for x in x_values]

# Membuat subplot
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Grafik hasil interpolasi Newton
axs[0].plot(x_data, y_data, 'ro', label='Data Asli')
axs[0].plot(x_values, y_newton, 'green', label='Interpolasi Newton')
axs[0].set_title('Interpolasi Polinomial Newton')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].legend()
axs[0].grid(True)

# Grafik polinom Lagrange dengan data asli berbentuk lingkaran
axs[1].plot(x_data, y_data, 'ro', label='Data Asli', zorder=5)
axs[1].plot(x_values, y_lagrange, label='Polinom Lagrange', color='blue')
axs[1].set_title('Polinom Lagrange')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')
axs[1].legend()
axs[1].grid(True)

# Menampilkan plot
plt.tight_layout()
plt.show()
