print('========================================')
print('DAFTAR HARGA :','\n Apel   : Rp 5000/Kg', '\n Jeruk  : Rp 8500/Kg', '\n Mangga : Rp 7800/Kg','\n Duku   : Rp 6500/Kg')
print('========================================')
try:
    data = {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500,
            'Apel': 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500  }
    print('Nama buah yang dibeli : ',end=' ')
    buah = input()
    x = data[buah]
    print('Berapa Kg             :', end=' ')
    kilo=int(input())
    print('========================================')
    print('Total Harga           :',x*kilo)
except KeyError:
    print('Maaf buah tidak tersedia atau input tidak valid')
except ValueError:
    print('Masukkan bilangan bulat saja')

