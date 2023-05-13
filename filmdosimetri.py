import matplotlib.pyplot as plt
import numpy as np

# Mengambil data dari tabel
gy = [0.0000, 0.1693, 0.3386, 0.5078, 0.6771, 0.8464, 1.0157, 1.1849, 1.3542, 1.5235, 1.6928, 1.8620, 2.0313, 2.2006, 2.3699]
red_channel = [0, 0.0292, 0.0533, 0.0740, 0.0884, 0.1124, 0.1259, 0.1355, 0.1547, 0.1635, 0.1692, 0.1920, 0.1956, 0.2012, 0.2195]
green_channel = [0, 0.0205, 0.0386, 0.0572, 0.0683, 0.0874, 0.1019, 0.1104, 0.1241, 0.1399, 0.1422, 0.1621, 0.1691, 0.1746, 0.1895]
blue_channel = [0, 0.0027, 0.0095, 0.0249, 0.0201, 0.0270, 0.0378, 0.0358, 0.0399, 0.0525, 0.0462, 0.0563, 0.0657, 0.0620, 0.0705]

# Melakukan plotting
plt.plot(gy, red_channel, label='Red Channel', color='red')
plt.plot(gy, green_channel, label='Green Channel', color='green')
plt.plot(gy, blue_channel, label='Blue Channel', color='blue')

plt.grid(True)

# Memberi judul pada grafik dan sumbu-sumbunya
plt.title('Grafik Sensitivitas Net OD terhadap Dosis')
plt.xlabel('Dosis (GY)')
plt.ylabel('netOD')

# Menampilkan legend
plt.legend()

# Menampilkan grafik
plt.show()


# Menghitung kurva polinomial orde 3
fit_red = np.polyfit(red_channel, gy, 3)
fit_green = np.polyfit(green_channel, gy, 3)
fit_blue = np.polyfit(blue_channel, gy, 3)

# Melakukan plotting data awal
plt.plot(gy, red_channel, 'o', label='Red Channel', color='red')
plt.plot(gy, green_channel, 'o', label='Green Channel', color='green')
plt.plot(gy, blue_channel, 'o', label='Blue Channel', color='blue')
plt.grid(True)

# Melakukan plotting kurva polinomial
r = np.linspace(0, max(red_channel), 50)
plt.plot(np.polyval(fit_red,r), r, color='red', linestyle='--')
g = np.linspace(0, max(green_channel), 50)
plt.plot(np.polyval(fit_green,g), g, color='green', linestyle='--')
b = np.linspace(0, max(blue_channel), 50)
plt.plot(np.polyval(fit_blue,b), b, color='blue', linestyle='--')

# Memberi judul pada grafik dan sumbu-sumbunya
plt.title('Grafik Kalibrasi Dosis terhadap netOD')
plt.xlabel('netOD')
plt.ylabel('Dosis (GY)')

# Menampilkan legend
plt.legend()

# Menampilkan grafik
plt.show()