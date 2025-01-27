import time
import numpy as np

def f(x):
    return 4 / (1 + x**2)

def simpson_13(a, b, n):
    if n % 2 == 1:
        raise ValueError("n must be an even number.")
    
    h = (b - a) / n
    x = a
    integral = f(a) + f(b)
    
    for i in range(1, n):
        x += h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    integral *= h / 3
    return integral

# Batas integral
a = 0
b = 1

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi N (jumlah segmen)
N_values = [10, 100, 1000, 10000]

# Menyimpan hasil
results = []

for n in N_values:
    start_time = time.time()
    pi_approx = simpson_13(a, b, n)
    end_time = time.time()
    
    # Menghitung galat RMS
    rms_error = np.sqrt((pi_approx - pi_reference)**2)
    
    # Mengukur waktu eksekusi
    execution_time = end_time - start_time
    
    results.append((n, pi_approx, rms_error, execution_time))

# Menampilkan hasil
print(f"{'N':>10} {'Pi Approximation':>20} {'RMS Error':>20} {'Execution Time (s)':>20}")
for result in results:
    print(f"{result[0]:>10} {result[1]:>20.15f} {result[2]:>20.15f} {result[3]:>20.15f}")
