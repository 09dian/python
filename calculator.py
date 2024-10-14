print("========================")
print("|Masukan Pilihan 1 - 4 |")
print("|1. Perkalian          |")
print("|2. Pembagian          |")
print("|3. Pertambahan        |")
print("|4. Pengurangan        |")
print("========================")

pilihan = input("Masuka Pilihan : ")
input_pilihan =int(pilihan)

def input_nilai():
   angka1= int(input("Masukan Angka Ke 1 : "))
   angka2= int(input("Masukan Angka Ke 2 : ")) 

if input_pilihan == 1:
   print("=====Perkalian=====")
   input_nilai()
   hasil=angka1*angka2
   print('Hasil Perkalian dari',angka1,'dibagi',angka2,'adalah = ',hasil)
elif input_pilihan == 2:
       
   print("=====Pembagian=====")
   angka1= int(input("Masukan Angka Ke 1 : "))
   angka2= int(input("Masukan Angka Ke 2 : "))
   hasil= angka1/angka2
   print('Hasil Pembagian dari',angka1,'dibagi',angka2,'adalah = ',hasil)
  
elif input_pilihan == 3:
    print("=====Pertambahan=====")
    angka1= int(input("Masukan Angka Ke 1 : "))
    angka2= int(input("Masukan Angka Ke 2 : "))
    hasil= angka1+angka2
    print('Hasil Penjumlahan dari',angka1,'ditambah',angka2,'adalah = ',hasil)
  
elif input_pilihan == 4:
    print("=====Pengurangan=====")
    angka1= int(input("Masukan Angka Ke 1 : "))
    angka2= int(input("Masukan Angka Ke 2 : "))
    hasil= angka1-angka2
    print('Hasil Pengurangan dari',angka1,'dikurang',angka2,'adalah = ',hasil)

      
else:
    print("Pilihan tidak ada")
