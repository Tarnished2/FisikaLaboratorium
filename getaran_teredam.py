import math
import numpy as np
import matplotlib.pyplot as plt

# 0. Masukkan nilai massa
m = float(input('masukkan nilai massa(kg) = '))

# 1. Menghitung Rasio Redaman Getaran
print('Perhitungan Rasio Redaman Getaran (δ)')
# δ0
X0 = float(input('masukkan nilai x0(m) = '))
X1 = float(input('masukkan nilai x1(m) = '))
X2 = float(input('masukkan nilai x2(m) = '))
X3 = float(input('masukkan nilai x3(m) = '))
X4 = float(input('masukkan nilai x4(m) = '))
X5 = float(input('masukkan nilai x5(m) = '))

δ0 = (math.log(X0/X1))/(((4*((math.pi)**2))+(math.log(X0/X1)**2)))**0.5
print('Hasil δ0 = ', δ0)

# δ1
δ1 = (math.log(X1/X2))/(((4*((math.pi)**2))+(math.log(X1/X2)**2)))**0.5
print('Hasil δ1 = ', δ1)

# δ2
δ2 = (math.log(X2/X3))/(((4*((math.pi)**2))+(math.log(X2/X3)**2)))**0.5
print('Hasil δ2 = ', δ2)

# δ3
δ3 = (math.log(X3/X4))/(((4*((math.pi)**2))+(math.log(X3/X4)**2)))**0.5
print('Hasil δ3 = ', δ3)

# δ4
δ4 = (math.log(X4/X5))/(((4*((math.pi)**2))+(math.log(X4/X5)**2)))**0.5
print('Hasil δ4 = ', δ4)

# 2. Menghitung Rasio Redaman Getaran Rata-rata
print('Perhitungan Rasio Redaman Getaran Rata-rata (δrata)')
δrata = (δ0+δ1+δ2+δ3+δ4)/5
print('Hasil δrata = ', δrata)

# 3. Menghitung Frekuensi Natural
print('Perhitungan Frekuensi Natural (fn)')
n = 5
# n adalah banyak getaran
t = float(input('masukkan nilai t = '))
# t adalah waktu yang diperlukan sistem untuk n getaran

fn = n/t
print('Hasil fn = ', fn)

# 4. Menghitung Frekuensi Sistem Teredam
print('Perhitungan Frekuensi Sistem Teredam (fd)')
fd = fn*((1-(δrata**2))**0.5)
print('Hasil fd = ', fd)

# 5. Menghitung Konstanta Pegas Sistem
print('Perhitungan Konstanta Pegas Sistem (k)')
k = m*((2*(math.pi)*fn)**2)
print('Hasil k = ', k)

# 6. Menghitung Koefisien Redaman Kritis
print('Perhitungan Koefisien Redaman Kritis (cc)')
cc = (4*m*k)**0.5
print('Hasil cc = ', cc)

# 7. Menghitung Koefisien Redaman Aktual
print('Perhitungan Koefisien Redaman Aktual (ca)')
ca = cc*δrata
print('Hasil ca = ', ca)

# Membuat Grafik Getaran Teredam
def f(t):
   return X0*((math.e)**(-(δrata*2*(math.pi)*fn*t)))*np.cos(2*(math.pi)*fn*t)

t = np.linspace(-20, 20, 150)

plt.plot(t, f(t), color='red')
plt.xlabel('waktu')
plt.ylabel('simpangan')
plt.title('Grafik Simpangan Fungsi Waktu')
plt.show()