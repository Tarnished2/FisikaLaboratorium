import math
import numpy as np
import matplotlib.pyplot as plt

#Grafik t/t0 terhadap kecepatan
print('Grafik t/t0 terhadap kecepatan')
x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
y = [1.01,1.04,1.01,1.25,1.16,1.3,1.43,1.49,2.4]
plt.scatter(x,y)
plt.plot(x, y, color='blue')
plt.xlabel('kecepatan')
plt.ylabel('t/t0')
plt.title('Grafik t/t0 terhadap kecepatan')
plt.show()

#Grafik L terhadap kecepatan
print('Grafik L terhadap kecepatan')
x = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
y = [2.05,2,1.95,1.9,1.8,1.65,1.45,1.25,0.9]
plt.scatter(x,y)
plt.plot(x, y, color='blue')
plt.xlabel('kecepatan')
plt.ylabel('L')
plt.title('Grafik L terhadap kecepatan')
plt.show()