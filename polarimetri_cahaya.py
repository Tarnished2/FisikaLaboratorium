import math
import numpy as np
import matplotlib.pyplot as plt

# 1. Menghitung konsentrasi eksperimen
print('Menghitung Konsentrasi Eksperimen')
m = float(input('masukkan nilai massa larutan = '))
L = 1 # dalam dL
ceks = m/L
print('Hasil Konsentrasi Eksperimen adalah ', ceks)

# 2. Menghitung Konsentrasi Teori
print('Menghitung Konsentrasi Teori')
thetalarutan = float(input('masukkan nilai sudut larutan = '))
thetaakuades = -48.4
alpha = abs(thetalarutan-thetaakuades)
l = 20
atd = 66.37
cteori = (100*alpha)/(l*atd)
print('Hasil Konsentrasi Teori adalah = ', cteori)

# 3. Menghitung Sudut Rotasi Spesifik
print('Menghitung Sudut Rotasi Spesifik')
atdspes = (100*alpha)/(l*cteori)
print('Hasil Sudut Rotasi Spesifik adalah = ', atdspes)

# 4. Menghitung Error Konsentrasi
print('Menghitung Error Konsentrasi')
errorc = (abs((cteori-ceks)/cteori))*100
print('Nilai error c adalah = ',errorc)

# 5. Plot Grafik Konsentrasi terhadap Sudut Rotasi
x = [0.1,0.2]
y = [99.5,167.4]
plt.plot(x, y, color='blue')
plt.xlabel('Konsentrasi')
plt.ylabel('Sudut Rotasi')
plt.title('Grafik Hubungan Konsentrasi terhadap Sudut Rotasi')
plt.show()