import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Biar folder images otomatis ada
os.makedirs("modul-1/images", exist_ok=True)

# Membuat data sembarang
penjualan = np.array([6, 5, 5, 4, 4, 3, 2, 2, 2, 1])
harga = np.array([16000, 18000, 27000, 34000, 50000, 68000, 65000, 81000, 85000, 90000])

# Print data
print("Data Penjualan :", penjualan)
print("Data Harga :", harga)

# Visualisasi data awal
plt.figure(figsize=(8, 5))
plt.scatter(penjualan, harga)
plt.title("Grafik data penjualan dan harga")
plt.xlabel("Penjualan")
plt.ylabel("Harga")
plt.savefig("modul-1/images/scatter_awal.png", bbox_inches="tight")
plt.show()

# Mengubah bentuk data penjualan agar sesuai untuk model
penjualan = penjualan.reshape(-1, 1)

# Membuat model regresi linear
linreg = LinearRegression()
linreg.fit(penjualan, harga)

# Menampilkan koefisien dan intercept
print("Koefisien :", linreg.coef_)
print("Intercept :", linreg.intercept_)

# Visualisasi hasil regresi
plt.figure(figsize=(8, 5))
plt.scatter(penjualan, harga, color="red")
plt.plot(penjualan, linreg.predict(penjualan))
plt.title("Visualisasi model regresi data penjualan dan harga")
plt.xlabel("Penjualan")
plt.ylabel("Harga")
plt.savefig("modul-1/images/regresi_modul1.png", bbox_inches="tight")
plt.show()