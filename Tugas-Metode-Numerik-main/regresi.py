import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# X = Jumlah Latihan Soal
# Y = Nilai Ujian
X = np.array([1, 2, 2, 2, 5, 6, 6, 6, 2, 0])
Y = np.array([91, 65, 45, 36, 66, 61, 63, 42, 61, 69])

# Metode Regresi Linear
def linear_regression(x, beta_0, beta_1):
    return beta_0 + beta_1 * x

# Metode Regresi Eksponensial
def exponential_regression(x, a, b, c):
    return a * np.exp(b * x) + c

# Plot titik data
plt.figure(figsize=(12, 6))

# Plot untuk Regresi Linear
plt.subplot(1, 2, 1)
plt.scatter(X, Y, color='blue', label='Data')
mean_X = np.mean(X)
mean_Y = np.mean(Y)
beta_1 = np.sum((X - mean_X) * (Y - mean_Y)) / np.sum((X - mean_X)**2)
beta_0 = mean_Y - beta_1 * mean_X
x_values_linear = np.linspace(min(X), max(X), 100)
y_values_linear = linear_regression(x_values_linear, beta_0, beta_1)
plt.plot(x_values_linear, y_values_linear, color='red', label='Regresi Linear')
plt.title('Regresi Linear')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Plot untuk Regresi Eksponensial
plt.subplot(1, 2, 2)
plt.scatter(X, Y, color='blue', label='Data')
popt, _ = curve_fit(exponential_regression, X, Y)
x_values_exponential = np.linspace(min(X), max(X), 100)
y_values_exponential = exponential_regression(x_values_exponential, *popt)
plt.plot(x_values_exponential, y_values_exponential, color='green', label='Regresi Eksponensial')
plt.title('Regresi Eksponensial')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Tampilkan plot
plt.tight_layout()
plt.show()

# Menghitung galat RMS
predicted_Y_linear = linear_regression(X, beta_0, beta_1)
rms_error_linear = np.sqrt(np.mean((Y - predicted_Y_linear)**2))
print("Galat RMS (Linear): ", rms_error_linear)

predicted_Y_exponential = exponential_regression(X, *popt)
rms_error_exponential = np.sqrt(np.mean((Y - predicted_Y_exponential)**2))
print("Galat RMS (Eksponensial): ", rms_error_exponential)
