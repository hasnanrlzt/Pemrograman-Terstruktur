try:
    file = open ('d:/data.txt', 'r')

# baca baris pertama dari file
#simpan ke dalam variabel bil1 sebagai interger

    bil1 = int(file.readline())

# Baca baris pertama dari file
# Simpan ke dalam variabel bil2 sebagai interger

    bil2 = int(file.readline())

# Hitung dan tampilkan hasil bagi

    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)

except FileNotFoundError:
    print('File tidak ditemukan')
except ZeroDivisionError:
    print('Tidak boleh pembagian dengan nol')

print('================================================')
try:
    file = open ('c:/data.txt', 'r')

# baca baris pertama dari file
#simpan ke dalam variabel bil1 sebagai interger

    bil1 = int(file.readline())

# Baca baris pertama dari file
# Simpan ke dalam variabel bil2 sebagai interger

    bil2 = int(file.readline())

# Hitung dan tampilkan hasil bagi

    hasil = bil1/bil2
    print(bil1, 'dibagi', bil2, 'sama dengan', hasil)

except FileNotFoundError:
    print('File tidak ditemukan')
except ZeroDivisionError:
    print('Tidak boleh pembagian dengan nol')

