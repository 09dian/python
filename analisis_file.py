import pandas as pd
import matplotlib.pyplot as plt

# Langkah 1: Membaca data dari file CSV
file_path = 'penjualan.csv'
df_penjualan = pd.read_csv(file_path)

# Langkah 2: Memeriksa dan memahami data
print("5 baris pertama data:")
print(df_penjualan.head())

print("\nInformasi statistik dasar:")
print(df_penjualan.describe())

print("\nInformasi umum tentang DataFrame:")
print(df_penjualan.info())

# Langkah 3: Melakukan analisis data dan visualisasi
plt.figure(figsize=(4, 3)) #ukuran
plt.bar(df_penjualan['Tahun'], df_penjualan['Penjualan'], color='green')

plt.title('Analisis Penurunan Penjualan (2018-2024)')
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.grid(axis='y')
plt.xticks(df_penjualan['Tahun'])

# Menampilkan grafik
plt.show()
