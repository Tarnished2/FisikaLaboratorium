import math
import numpy as np
import matplotlib.pyplot as plt

print('TETES MINYAK MILLIKAN')

# 1. mencari jari-jari butir minyak
η = 1.983*(10**(-5))
g = 9.8 #percepatan gravitasi
d1 = 0.005 #jarak d1
t1 = float(input('masukkan nilai waktu(t1) = ')) #t1 adalah waktu yang dibutuhkan pada d1
v1 = d1/t1 #kecepatan untuk menempuh d1
print('v1 = ', v1)
rho = float(input('masukkan nilai densitas minyak = ')) #densitas minyak
rhou = 1.2 #densitas udara

r = (9*η*v1)/(2*g*(rho-rhou))
print('nilai r = ',r)

# 2. mencari muatan listrik butir minyak
d2 = 0.005 #jarak d2
t2 = float(input('masukkan nilai waktu(t2) = ')) #t2 adalah waktu yang dibutuhkan pada d2
v2 = d2/t2 #kecepatan untuk menempuh d2
print('v2 = ', v2)
d = 0.016 #jarak antar pelat
V = 5500 #balancing voltage

q = 6*math.pi*η*r*(v1+v2)*(d/V)
print('nilai q = ',q)

print('EKSPERIMEN FRANCK-HERTZ')
# 3. mencari energi eksitasi atom
e = -1.602*(10**(-19))
n = float(input('masukkan nilai n = '))
Vn = n
Vn_1 = n+1

En = e*(Vn_1-Vn)
En_1 = En
print('nilai En = ', En)

# 4. menghitung panjang gelombang teremisi
h = 6.62*(10**(-34))
c = 3*(10*8)

lamda = (h*c)/(En_1-En)
print('Hasil lambda =', lamda)

# plot grafik eksperimen gas neon
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
y = [0.5,3.3,5.2,7.2,1.8,7,8.9,12,14.2,4.2,7.6,12,16,18.3,5.6,10.4,18,20,22.2,6.1,11,22,25,26.6,8,14,23,28,29,11,16,25,30,32.1,19,12,29,33,35,29]
plt.plot(x,y)
plt.xlabel('Ub')
plt.ylabel('Ia')
plt.title('Percobaan Franck-Hertz dengan Merkuri')
plt.show()

# plot grafik eksperimen gas merkuri
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
b = [0.4,3.4,6.5,8.1,10,12,13,14,17,19,20,20,23,23,26,27,28,26,6.1,17,19,23,24,25,26,27,26,25,27,28,30,32,29,30,30,29,25,9.8,22,27]
plt.plot(a,b)
plt.xlabel('Ub')
plt.ylabel('Ia')
plt.title('Percobaan Franck-Hertz dengan Neon')
plt.show()