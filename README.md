# Simple Linear Regression with Python 📈

Implementasi **Simple Linear Regression** menggunakan Python berdasarkan 2 modul praktikum:

- **Modul 1** — Regresi linear sederhana dengan **data sembarang (custom)**
- **Modul 2** — Regresi linear sederhana dengan **dataset FuelConsumptionCo2**

Project ini saya buat menggunakan **VS Code**, dengan visualisasi memakai **Matplotlib** dan model regresi dari **Scikit-learn**.

---

## 📖 Overview

Dalam *machine learning*, **supervised learning** adalah metode pembelajaran yang menggunakan data berlabel untuk melatih model agar bisa melakukan prediksi. Salah satu bentuk *supervised learning* adalah **regresi**, yaitu teknik untuk memprediksi nilai numerik kontinu.

Pada project ini, saya menggunakan **simple linear regression**, yaitu model regresi linear dengan **1 variabel independen (X)** dan **1 variabel dependen (Y)**.

---

## 🛠️ Tech Stack
- **Python**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Scikit-learn**
- **VS Code**

---

## 📁 Project Structure
```bash
simple-linear-regression/
├── modul-1/
│   ├── modul1.py
│   └── images/
│       ├── scatter_awal.png
│       └── regresi_modul1.png
├── modul-2/
│   ├── modul2.py
│   ├── FuelConsumptionCo2.csv
│   └── images/
│       ├── fuel_vs_emission.png
│       ├── engine_vs_emission.png
│       ├── train_engine_vs_emission.png
│       └── regresi_modul2.png
└── README.md
````

-----

## 🚀 Installation & How to Run

### 1\. Clone & Setup Environment

Clone repo ini, lalu buat dan aktifkan virtual environment:

**Windows (PowerShell):**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2\. Install Dependencies

```bash
pip install numpy pandas matplotlib scikit-learn
```

### 3\. Run the Code

**Jalankan Modul 1:**

```bash
python modul-1/modul1.py
```

**Jalankan Modul 2:**

```bash
python modul-2/modul2.py
```

-----

## 📊 Modul 1 — Simple Linear Regression with Custom Data

### Deskripsi

Pada modul ini, saya menggunakan data sederhana berupa angka penjualan dan harga untuk melihat hubungan antara kedua variabel menggunakan metode simple linear regression.

**Data yang digunakan:**

  - `penjualan` = `[6, 5, 5, 4, 4, 3, 2, 2, 2, 1]`
  - `harga` = `[16000, 18000, 27000, 34000, 50000, 68000, 65000, 81000, 85000, 90000]`

### Output Visualisasi

**1. Scatter Plot Awal** 

<img width="713" height="470" alt="image" src="https://github.com/user-attachments/assets/9efbc7c9-f623-41ec-937d-a0a60d64a45b" />

**2. Hasil Regresi Linear** 

<img width="713" height="470" alt="image" src="https://github.com/user-attachments/assets/cb814d86-2111-47f2-bf88-cdc1026716c5" />

### 💡 Insight Modul 1

Dari hasil visualisasi, data menunjukkan kecenderungan hubungan linear negatif antara penjualan dan harga. Garis regresi yang terbentuk menurun, yang berarti pada data ini ketika nilai penjualan meningkat, harga cenderung menurun.

-----

## 🚗 Modul 2 — Simple Linear Regression with Dataset

### Deskripsi

Pada modul ini, saya menggunakan dataset nyata `FuelConsumptionCo2.csv` untuk membuat model regresi linear sederhana. Fokus analisis diarahkan pada hubungan antara ukuran mesin kendaraan (`ENGINESIZE`) dan emisi CO2 (`CO2EMISSIONS`).

**Kolom yang dianalisis:** `['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_CITY', 'CO2EMISSIONS']`

### Output Visualisasi

**1. Fuel Consumption City vs CO2 Emissions** 

<img width="695" height="470" alt="image" src="https://github.com/user-attachments/assets/7ea25b8f-d42b-410a-a2df-59740a75d9c7" />

**2. Engine Size vs CO2 Emissions** 

<img width="695" height="470" alt="image" src="https://github.com/user-attachments/assets/79a9b164-89e6-4378-bf6b-f0e0ed9fe63e" />

**3. Training Data Visualization** 

<img width="695" height="470" alt="image" src="https://github.com/user-attachments/assets/ca30bb8e-83ed-4390-a4af-a30d6311257f" />

**4. Hasil Regresi Linear** 

<img width="695" height="470" alt="image" src="https://github.com/user-attachments/assets/a4430f5c-e22e-4270-a129-ea5b8b0800de" />

### 💡 Insight Modul 2

Dari visualisasi data, hubungan antara `FUELCONSUMPTION_CITY` dan `CO2EMISSIONS` terlihat positif. Hal yang sama juga terlihat pada hubungan antara `ENGINESIZE` dan `CO2EMISSIONS`.

Setelah model dilatih, garis regresi menunjukkan tren naik. Artinya, semakin besar ukuran mesin kendaraan, maka emisi CO2 cenderung semakin tinggi pada dataset yang digunakan.

-----

## 🎯 Kesimpulan

Project ini berhasil mengimplementasikan Simple Linear Regression dalam dua skenario (data manual dan dataset CSV). Dari ekplorasi ini, dapat dipahami bahwa:

  - Regresi linear sederhana efektif digunakan untuk memodelkan hubungan antara 1 variabel input (X) dan 1 variabel output (Y).
  - Visualisasi *scatter plot* sangat membantu untuk melihat pola hubungan data secara kasat mata.
  - Garis regresi mempermudah kita memahami arah hubungan antar variabel.

Modul 1 membantu memahami konsep dasar dengan data manual, sedangkan Modul 2 memperlihatkan implementasi langsung pada dataset yang lebih realistis.

```
