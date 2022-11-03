import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# menentukan indeks bias prisma
sudut = float(input('masukkan nilai sudut yang didapat '))
delta = sudut - 272.4
print('nilai delta adalah',delta)

n = (np.sin(0.5*(np.radians(delta)+(np.pi/3))))/(np.sin(np.pi/6))
print('nilai indeks bias adalah ',n)

# plot grafik antara indeks bias prisma dengan 1/lambda ref squared helium
x = [2.131*10**(-6),2.972*10**(-6),3.533*10**(-6),4.526*10**(-6),5.806*10**(-6)] #lambda ref squared
y = [1.756,1.76,1.764,1.766,1.768] #indeks bias
slope1, intercept1, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope1 * x + intercept1

mymodel = list(map(myfunc, x))
plt.xlabel('lambda ref squared')
plt.ylabel('indeks bias')
plt.title('hubungan indeks bias dengan 1/lambda ref^2 pada helium')
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()
print('gradien helium adalah ',slope1)
print('titik potong sumbu y adalah ',intercept1)

# menghitung panjang gelombang gas helium
m = slope1
c = intercept1
lamdah = ((m)/(n-c))**0.5
print('hasil panjang gelombangnya adalah ',lamdah)

# menghitung energi dari spektrum helium
h = (6.626)*(10**(-34))
c = 3*(10**8)
Eh = (h*c)/(lamdah*(10**-9))
print('energinya adalah ',Eh)

# plot grafik hubungan energi dengan panjang gelombang helium
a = [607.74,557.15,485.39,446.89,425.87] #panjang gelombang
b = [3.27*(10**(-19)),3.567*(10**(-19)),4.095*(10**(-19)),4.448*(10**(-19)),4.667*(10**(-19))] #energi
plt.plot(a,b)
plt.xlabel('panjang gelombang')
plt.ylabel('energi')
plt.title('Hubungan panjang gelombang dengan energi pada helium')
plt.show()

# plot grafik antara indeks bias prisma dengan 1/lambda ref squared neon
x = [2.131*10**(-6),2.732*10**(-6),2.972*10**(-6),3.533*10**(-6)] #lambda ref squared
y = [1.778,1.779,1.78,1.781] #indeks bias
slope2, intercept2, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope2 * x + intercept2

mymodel = list(map(myfunc, x))
plt.xlabel('lambda ref squared')
plt.ylabel('indeks bias')
plt.title('hubungan indeks bias dengan 1/lambda ref^2 pada neon')
plt.scatter(x,y)
plt.plot(x,mymodel)
plt.show()
print('gradien neon adalah ',slope2)
print('titik potong sumbu y adalah ',intercept2)

# menghitung panjang gelombang gas neon
m = slope2
c = intercept2
lamdan = ((m)/(n-c))**0.5
print('hasil panjang gelombangnya adalah ',lamdan)

# menghitung energi dari spektrum neon
h = (6.626)*(10**(-34))
c = 3*(10**8)
En = (h*c)/(lamdan*(10**-9))
print('energinya adalah ',En)

# plot grafik hubungan energi dengan panjang gelombang neon
a = [627.67,587.1,553.56,525.22] #panjang gelombang
b = [3.167*(10**(-19)),3.385*(10**(-19)),3.59*(10**(-19)),3.784*(10**(-19))] #energi
plt.plot(a,b)
plt.xlabel('panjang gelombang')
plt.ylabel('energi')
plt.title('Hubungan panjang gelombang dengan energi pada neon')
plt.show()