import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#menentukan diameter cincin
L = float(input('masukkan nilai jarak kiri = '))
R = float(input('masukkan nilai jarak kanan = '))
D = abs(L-R)
D_kuadrat = D**2
m = float(input('orde ke-'))
r = 2500
print('diameternya adalah ',D)
print('nilai diameter kuadrat adalah',D_kuadrat)

#menentukan panjang gelombang
lamda = (D_kuadrat)/(4*r*m)
print('nilai panjang gelombang adalah ',lamda)

#plot grafik pengulangan 1
x = [1,2,3,4,5,6,7,8,9,10]
y = [6.65,11.15,15.13,20.7,26.5,30.69,38.44,43.42,47.74,49.28]
slope1, intercept1, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope1 * x + intercept1

mymodel = list(map(myfunc, x))
plt.xlabel('orde cincin')
plt.ylabel('diameter kuadrat')
plt.title('orde cincin terhadap diameter kuadrat percobaan ke-1')
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()
print('gradien 1 adalah ',slope1)
print('koef 1 adalah ',intercept1)
lref1 = slope1/(4*2500)
print('panjang gel referensi pengulangan 1 adalah ',lref1)

#plot grafik pengulangan 2
x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = [3.53,10.49,15.21,19.89,24.2,28.94,32.71,38.56,43.03,47.74]
slope2, intercept2, r, p, std_err = stats.linregress(x1, y1)

def myfunc(x1):
  return slope2 * x1 + intercept2

mymodel = list(map(myfunc, x1))
plt.xlabel('orde cincin')
plt.ylabel('diameter kuadrat')
plt.title('orde cincin terhadap diameter kuadrat percobaan ke-2')
plt.scatter(x1,y1)
plt.plot(x1,mymodel)
plt.show()
print('gradien 2 adalah ',slope2)
print('koef 2 adalah ',intercept2)
lref2 = slope2/(4*2500)
print('panjang gel referensi pengulangan 2 adalah ',lref2)

#plot grafik pengulangan 3
x2 = [1,2,3,4,5,6,7,8,9,10]
y2 = [3.42,10.56,14.28,18.92,25.1,30.03,34.1,38.31,44.08,48.16]
slope3, intercept3, r, p, std_err = stats.linregress(x2, y2)

def myfunc(x2):
  return slope3 * x2 + intercept3

mymodel = list(map(myfunc, x2))
plt.xlabel('orde cincin')
plt.ylabel('diameter kuadrat')
plt.title('orde cincin terhadap diameter kuadrat percobaan ke-3')
plt.scatter(x2,y2)
plt.plot(x2,mymodel)
plt.show()
print('gradien 3 adalah ',slope3)
print('koef 3 adalah ',intercept3)
lref3 = slope3/(4*2500)
print('panjang gel referensi pengulangan 3 adalah ',lref3)