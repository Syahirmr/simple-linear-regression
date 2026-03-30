import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Optional: biar hasil split train/test konsisten setiap dijalankan
np.random.seed(42)

# Path folder modul-2
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "FuelConsumptionCo2.csv")
images_dir = os.path.join(base_dir, "images")
os.makedirs(images_dir, exist_ok=True)

# Membaca data CSV
df = pd.read_csv(csv_path)

# Menampilkan 5 baris pertama
print("5 baris pertama dataset:")
print(df.head())

# Ambil kolom yang dibutuhkan
cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']]

print("\n9 baris pertama kolom terpilih:")
print(cdf.head(9))

# Plot Fuel Consumption City vs CO2 Emissions
plt.figure(figsize=(8, 5))
plt.scatter(cdf.FUELCONSUMPTION_CITY, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("FUELCONSUMPTION_CITY")
plt.ylabel("Emission")
plt.title("Fuel Consumption City vs CO2 Emissions")
plt.savefig(os.path.join(images_dir, "fuel_vs_emission.png"), bbox_inches="tight")
plt.show()

# Plot Engine Size vs CO2 Emissions
plt.figure(figsize=(8, 5))
plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.title("Engine Size vs CO2 Emissions")
plt.savefig(os.path.join(images_dir, "engine_vs_emission.png"), bbox_inches="tight")
plt.show()

# Splitting data train dan test
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

print("\nJumlah data train:", len(train))
print("Jumlah data test :", len(test))

# Visualisasi data training
plt.figure(figsize=(8, 5))
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.title("Training Data: Engine Size vs CO2 Emissions")
plt.savefig(os.path.join(images_dir, "train_engine_vs_emission.png"), bbox_inches="tight")
plt.show()

# Membuat model regresi linear
regr = LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])

regr.fit(train_x, train_y)

# Koefisien model
print("\nCoefficients:", regr.coef_)
print("Intercept:", regr.intercept_)

# Plot hasil regresi
plt.figure(figsize=(8, 5))
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color='blue')
plt.plot(train_x, regr.coef_[0][0] * train_x + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.title("Linear Regression: Engine Size vs CO2 Emissions")
plt.savefig(os.path.join(images_dir, "regresi_modul2.png"), bbox_inches="tight")
plt.show()