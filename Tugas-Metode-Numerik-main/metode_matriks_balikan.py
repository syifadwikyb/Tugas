import numpy as np

print ("\n====Ini adalah tugas metode numerik====\n"
       "Syifa Dwiky Basamala\t21120122120008\n")

def metode_matriks_balikan(A, b):

  # Hitung determinan matriks A
  det_A = np.linalg.det(A)

  # Periksa apakah matriks A singular
  if det_A == 0:
    raise Exception("Matriks A singular!")

  # Hitung matriks balikan A^-1
  A_inv = np.linalg.inv(A)

  # Hitung solusi x
  x = np.dot(A_inv, b)

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
  x = metode_matriks_balikan(A, b)
  print("Solusi:", x)
except Exception as e:
  print("Terjadi kesalahan:", e)
