lokasi = open('c:\Ganjilgenap.txt', 'r')
data   = lokasi.readlines()
bilgenap  = []
bilganjil = []
for x in range(len(data)):
    num = data[x]
    if (int (num) %2) == 0 :
        bilgenap  = bilgenap + [num]
        hasilgenap= len(bilgenap)
    else :
        bilganjil  = bilganjil + [num]
        hasilganjil= len(bilganjil)
lokasi.close()
print('Banyaknya bilangan genap  : ', hasilgenap)
print('Banyaknya bilangan ganjil : ', hasilganjil)

