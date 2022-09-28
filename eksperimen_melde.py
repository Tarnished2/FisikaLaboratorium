import math
import numpy as np
import matplotlib.pyplot as plt

print('TALI KUNING')
# menghitung gaya tegangan tali
print('GAYA TEGANGAN TALI KUNING')
M = float(input('masukkan nilai massa total beban = '))
g = 9.8

F = M*g
print('hasil gaya tegangan tali kuning adalah = ', F)

# menghitung rapat massa linear
print('RAPAT MASSA LINEAR TALI KUNING')
m = 0.00142
L = 1.5

mu = m/L
print('rapat massa linear tali kuning adalah = ', mu)

# menghitung kecepatan gelombang
print('KECEPATAN GELOMBANG TALI KUNING')
v = F/mu
print('kecepatan gelombang tali kuning adalah = ', v)

# menghitung panjang gelombang ideal
print('PANJANG GELOMBANG IDEAL TALI KUNING')
f = 50

lambda1 = (1/f)*((F/mu)**0.5)
print('panjang gelombang ideal tali kuning adalah = ', lambda1)

# menghitung panjang gelombang bergantung segmen
print('PANJANG GELOMBANG BERGANTUNG SEGMEN TALI KUNING')
n = float(input('masukkan banyak gelombang = '))
L = float(input('masukkan panjang gelombang percobaan = '))

lambda2 = L/n
print('hasil panjang gelombang bergantung segmen adalah = ', lambda2)

print('TALI MERAH')
# menghitung gaya tegangan tali
print('GAYA TEGANGAN TALI MERAH')
M = float(input('masukkan nilai massa total beban = '))
g = 9.8

F = M*g
print('hasil gaya tegangan tali MERAH adalah = ', F)

# menghitung rapat massa linear
print('RAPAT MASSA LINEAR TALI MERAH')
m = 0.00154
L = 1.5

mu = m/L
print('rapat massa linear tali merah adalah = ', mu)

# menghitung kecepatan gelombang
print('KECEPATAN GELOMBANG TALI MERAH')
v = F/mu
print('kecepatan gelombang tali merah adalah = ', v)

# menghitung panjang gelombang ideal
print('PANJANG GELOMBANG IDEAL TALI MERAH')
f = 50

lambda1 = (1/f)*((F/mu)**0.5)
print('panjang gelombang ideal tali merah adalah = ', lambda1)

# menghitung panjang gelombang bergantung segmen
print('PANJANG GELOMBANG BERGANTUNG SEGMEN TALI MERAH')
n = float(input('masukkan banyak gelombang = '))
L = float(input('masukkan panjang gelombang percobaan = '))

lambda2 = L/n
print('hasil panjang gelombang bergantung segmen adalah = ', lambda2)

# mencari grafik
print('GRAFIK HUBUNGAN TEGANGAN TALI DENGAN KECEPATAN GELOMBANG KUADRAT TALI KUNING')
# gaya tegangan tali sebagai sumbu y
# v kuadrat sebagai sumbu x
x = [73282.27,590653.73,890175.26]
y = [0.25627,0.727552,0.893172]
plt.plot(x, y, color='yellow')
plt.xlabel('v kuadrat')
plt.ylabel('gaya tegangan tali')
plt.title('Grafik Hubungan Tegangan Tali dengan Kecepatan Gelombang Kuadrat Tali Kuning')
plt.show()

print('GRAFIK HUBUNGAN RAPAT MASSA LINEAR DENGAN KECEPATAN GELOMBANG KUADRAT TALI KUNING')
# mu sebagai sumbu y
# v kuadrat sebagai sumbu x
x = [73282.27,590653.73,890175.26]
y = [0.0009467,0.0009467,0.0009467]
plt.plot(x, y, color='yellow')
plt.xlabel('v kuadrat')
plt.ylabel('rapat massa linear')
plt.title('Grafik Hubungan Rapat Massa Linear dengan Kecepatan Gelombang Kuadrat Tali Kuning')
plt.show()

print('GRAFIK HUBUNGAN TEGANGAN TALI DENGAN KECEPATAN GELOMBANG KUADRAT TALI MERAH')
# gaya tegangan tali sebagai sumbu y
# v kuadrat sebagai sumbu x
x = [62306.64,502190.49,804558.76]
y = [0.25627,0.727552,0.893172]
plt.plot(x, y, color='red')
plt.xlabel('v kuadrat')
plt.ylabel('gaya tegangan tali')
plt.title('Grafik Hubungan Tegangan Tali dengan Kecepatan Gelombang Kuadrat Tali Merah')
plt.show()

print('GRAFIK HUBUNGAN RAPAT MASSA LINEAR DENGAN KECEPATAN GELOMBANG KUADRAT TALI MERAH')
# mu sebagai sumbu y
# v kuadrat sebagai sumbu x
x = [62306.64,502190.49,804558.76]
y = [0.0010267,0.0010267,0.0010267]
plt.plot(x, y, color='red')
plt.xlabel('v kuadrat')
plt.ylabel('rapat massa linear')
plt.title('Grafik Hubungan Rapat Massa Linear dengan Kecepatan Gelombang Kuadrat Tali Merah')
plt.show()