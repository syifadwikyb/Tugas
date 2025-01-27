import numpy as np

print ("\n====Ini adalah tugas metode numerik====\n"
       "Syifa Dwiky Basamala\t21120122120008\n")

def metode_dekomposisi_lu_gauss(A, b):
    
  n = A.shape[0]

  # Dekomposisi LU
  L, U = np.zeros((n, n)), np.zeros((n, n))
  for i in range(n):
    for j in range(i + 1):
      if j == 0:
        L[i, 0] = A[i, 0] / U[0, 0]
        U[i, 0] = A[i, 0]
      else:
        L[i, j] = (A[i, j] - np.dot(L[i, :j], U[:j, j])) / U[j, j]
        U[i, j] = A[i, j] - np.dot(L[i, :j], U[:j, j])

  # Substitusi maju
  y = np.zeros(n)
  for i in range(n):
    y[i] = b[i] - np.dot(L[i, :i], y[:i])

  # Substitusi mundur
  x = np.zeros(n)
  for i in range(n - 1, -1, -1):
    x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

  return x

# Inputan dari pengguna
while True:
  try:
    n = int(input("Masukkan jumlah persamaan (n): "))
    if n <= 0:
      raise ValueError("n harus bilangan bulat positif!")
    break
  except ValueError:
    print("Input tidak valid. Masukkan bilangan bulat positif untuk n.")

A = np.zeros((n, n))
for i in range(n):
  for j in range(n):
    while True:
      try:
        A[i, j] = float(input(f"Masukkan elemen A[{i+1},{j+1}]: "))
        break
      except ValueError:
        print("Input tidak valid. Masukkan bilangan real untuk elemen matriks.")

b = np.zeros(n)
for i in range(n):
  while True:
    try:
      b[i] = float(input(f"Masukkan elemen b[{i+1}]: "))
      break
    except ValueError:
      print("Input tidak valid. Masukkan bilangan real untuk elemen vektor.")

try:
  x = metode_dekomposisi_lu_gauss(A, b)
  print("Solusi:", x)
except Exception as e:
  print("Terjadi kesalahan:", e)
