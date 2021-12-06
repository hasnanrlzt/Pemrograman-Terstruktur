lokasiawal = open('c:\Data Bilangan.txt', 'r')
data = lokasiawal.readlines()
lokasiakhir = open('c:\Penjumlahan Bilangan.txt', 'w')

for soal in  data:
    langkah1 = soal.split('|')
    bil1    = langkah1[0]
    bil2    = langkah1[1]
    langkah2 = int(bil1) + int(bil2)
    langkah3 = str(langkah2)
    lokasiakhir.write(langkah3)
    lokasiakhir.write('\n')

lokasiakhir.close()
hasil = open('c:\Penjumlahan Bilangan.txt', 'r')
print(hasil.read())
hasil.close

