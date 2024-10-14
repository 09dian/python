import pandas as pd
import matplotlib.pyplot as plt

# Langkah 1: Membuat dataset penjualan
data_penjualan = {
    'Tahun': [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Penjualan': [1500, 1400, 1300, 1200, 1100, 1000, 900]  # Contoh data penjualan
}

# Mengonversi dictionary ke DataFrame
df_penjualan = pd.DataFrame(data_penjualan)

# Langkah 2: Analisis penurunan penjualan
plt.figure(figsize=(10, 6))
plt.bar(df_penjualan['Tahun'], df_penjualan['Penjualan'],color='b')

plt.title('Analisis Penurunan Penjualan (2018-2024)')
plt.xlabel('Tahun')
plt.ylabel('Penjualan')
plt.grid(True)
plt.xticks(df_penjualan['Tahun'])

# Menampilkan grafik
plt.show()

# Menampilkan DataFrame untuk referensi
print(df_penjualan)
