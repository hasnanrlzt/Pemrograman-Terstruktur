print('----------------------------')
print('  PROGRAM HITUNG RATA-RATA  ')
print('----------------------------')
jawab  = True
sum    = 0
jumlah = 0

while (jawab == True):
    try:
        bil = int(input('Masukkan bilangan bulat        : '))
        sum += bil
        jumlah += 1

        pilih = str(input('Lagi y/n?                       :'))

        if (pilih == 'y'):
            jawab = True

        elif (pilih == 'n'):
            jawab  = False

        else :
            print('Input tidak valid, harus berupa y/n')

    except ValueError:
        print('Bukan bilangan bulat')
        continue

rerata = sum / jumlah
print("Rata-ratanya adalah              :", rerata)

