import statistics


jumlah_data = int(input("Masukkan jumlah data yang ingin diinput: "))

# Membuat list untuk menyimpan data
data_list = []

print("==========================")
print("|Masukan Pilihan 1 - 3   |")
print("|1. Mean (Rata-Rata)     |")
print("|2. Modus (Banyak Niali) |")
print("|3. Median (Nilai Tengah)|")
print("==========================")

pilihan = input("Masuka Pilihan : ")
input_pilihan =int(pilihan)

for i in range(jumlah_data):
        data = float(input(f"Masukkan data ke-{i + 1}: "))
        data_list.append(data)
        
if input_pilihan==1:
    mean_value = statistics.mean(data_list)
    print(f"Nilai Rata-Rata Adalah: {mean_value}")
    
elif input_pilihan==2:
    mode_value = statistics.mode(data_list)
    print(f"Nilai Modus Adalah: {mode_value}")
    
elif input_pilihan==2:
    median_value = statistics.median(data_list)
    print(f"Nilai Tengah Adalah Adalah: {median_value}")
else:
    print("Pilihan Tidak Ada")