import math
import numpy as np
import matplotlib.pyplot as plt

# mencari energi kinetik maksimum
e = -1.6*(10**-19)
V0 = float(input('masukkan nilai retarding voltage = '))
KEmax = e*V0
print('nilai KEmax adalah',KEmax)

# mencari konstanta Planck
c = 3*(10**8)
W = (4.7)*(abs(e))
lamda = float(input('masukkan nilai panjang gelombang = '))
v = c/(lamda*(10**-9))
print('nilai v adalah',v)
h = (KEmax+W)/(v)
print('nilai h adalah = ', h)

# membuat grafik arus terhadap tegangan retardasi variasi panjang gelombang
x = [-10,-9.5,-9,-8.5,-8,-7.5,-7,-6.5,-6,-5.5,-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0]
a = [0,0,0,0,0,0.54,1.74,3.04,4.29,5.54,6.74,8.04,9.29,10.54,11.74,13.04,14.29,15.54,16.74,18.4,19.26]
b = [0,0,0,0,0,0,0,0,0,0,0.38,1.63,2.88,4.13,5.38,6.63,7.88,9.13,10.38,11.63,12.88]
c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0.19,1.44,2.69,3.94,5.19,6.44,7.69,8.94]
d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.89,2.14,3.39,4.64,5.89]

plt.plot(x, a, b, c, d)
plt.xlabel('tegangan retardasi')
plt.ylabel('arus')
plt.title('Grafik Hubungan arus terhadap tegangan retardasi dengan variasi panjang gelombang')
plt.show()

# membuat grafik arus terhadap tegangan retardasi variasi intensitas cahaya
x = [-10,-9.5,-9,-8.5,-8,-7.5,-7,-6.5,-6,-5.5,-5,-4.5,-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0]
a = [0,0,0,0,0,0,0,0,0,0,0,0,0,0.08,0.58,1.08,1.58,2.08,2.58,3.08,3.58]
b = [0,0,0,0,0,0,0,0,0,0,0,0,0,0.12,0.87,1.62,2.37,3.12,3.87,4.62,5.37]
c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0.15,1.15,2.15,3.15,4.15,5.15,6.15,7.15]
d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0.19,1.44,2.69,3.94,5.19,6.44,7.69,8.94]

plt.plot(x, a, b, c, d)
plt.xlabel('tegangan retardasi')
plt.ylabel('arus')
plt.title('Grafik Hubungan arus terhadap tegangan retardasi dengan variasi intensitas cahaya')
plt.show()