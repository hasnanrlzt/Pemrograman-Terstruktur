print('========================================')
print('DAFTAR HARGA :','\n Apel   : Rp 5000/Kg', '\n Jeruk  : Rp 8500/Kg',
      '\n Mangga : Rp 7800/Kg','\n Duku   : Rp 6500/Kg')
print('========================================')

try:
    data = {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500,
            'Apel': 5000, 'Jeruk' : 8500, 'Mangga' : 7800, 'Duku' : 6500 }
    print('Nama buah yang dibeli      : ',end=' ')
    buah = input()
    d = data[buah]
    print('Berapa Kg                  :', end=' ')
    kilo = int(input())
    x = d*kilo
    print('Beli Buah yang lain? (y/n) : ',end=' ')
    a=input()
    while True:
        if a == 'y'or a == 'Y':
            print('Nama buah yang dibeli      : ',end=' ')
            buah = input()
            c = data[buah]
            print('Berapa Kg                  :', end=' ')
            kg1 = int(input())
            print('Beli Buah yang lain? (Y/N) :')
            a = input()
            d += c
            x1 = c*kg1
            x += x1
            if a == 'y'or a == 'Y':
                continue
            if a == 'n'or a == 'N':
                break
        if a == 'n'or a == 'N':
            break
        else:
            print('input tidak valid')
            exit()
    print('===============================================')
    print('Total Harga              ',x)
except KeyError:
    print('Buah tidak tersedia atau input tidak valid')
except ValueError:
    print('Masukkan bilangan bulat saja')

