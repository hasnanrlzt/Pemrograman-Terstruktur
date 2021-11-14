data = {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }
print('Menu')
print('A. Tambah data buah \nB. Beli buah \nC. Hapus data Buah')
print('Pilihan Menu :',end=' ')
b = input()
if b == 'a' or b == 'A':
    c = input('Masukkan nama buah       : ')
    if c in data:
        print('Buah Sudah Ada')
    else:
        print('Harga Buah               : ',end=' ')
        harga = int(input())
        data[c] = harga
        print('Daftar Buah dan Harganya :')
        for a in data.items():
            print(a)
        print('Ingin menambah data buah yang lain? (y/n) : ', end=' ')
        a = input()
        while True:
            if a == 'y' or a == 'Y':
                if b == 'a' or b == 'A':
                    c = input('Masukkan nama buah : ')
                    if c in data:
                        print('Buah Sudah Ada')
                    else:
                        print('Harga Buah : ', end=' ')
                        harga = int(input())
                        data[c] = harga
                        print('Daftar Buah dan Harganya :')
                        for a in data.items():
                            print(a)
                        print('Ingin menambah data buah yang lain? (y/n) : ', end=' ')
                        a = input()
                        if a == 'y' or a == 'Y':
                            continue
                        if a == 'n' or a == 'N':
                            break
            if a == 'n' or a == 'N':
                break
            else:
                print('Maaf input tidak valid !!!!!')
                print('Ingin menambah data buah yang lain? (y/n) : ', end=' ')
                a = input()
                if a == 'y' or a == 'Y':
                    if b == 'a' or b == 'A':
                        c = input('Masukkan nama buah : ')
                        if c in data:
                            print('Buah Sudah Ada')
                        else:
                            print('Harga Buah : ', end=' ')
                            harga = int(input())
                            data[c] = harga
                            print('Daftar Buah dan Harganya :')
                            for a in data.items():
                                print(a)
                            print('Ingin menambah data buah yang lain? (y/n) : ', end=' ')
                            a = input()
                            if a == 'y' or a == 'Y':
                                continue
                            if a == 'n' or a == 'N':
                                break
if b == 'b' or b == 'B':
    try:
        print('========================================')
        print('DAFTAR HARGA :', '\n Apel   : Rp 5000/Kg', '\n Jeruk  : Rp 8500/Kg',
              '\n Mangga : Rp 7800/Kg', '\n Duku   : Rp 6500/Kg')
        print('========================================')
        data = {'apel': 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500 }
        print('nama buah yang dibeli      : ',end=' ')
        buah1 = input()
        d = data[buah1]
        print('Berapa Kg                  : ', end=' ')
        kilo = int(input())
        x = d*kilo
        print('Beli Buah yang lain? (y/n) :',end=' ')
        a = input()
        while True:
            if a == 'y'or a == 'Y':
                print('nama buah yang dibeli : ',end=' ')
                buah = input()
                c = data[buah]
                print('Berapa Kg             :  ', end=' ')
                kilo1 = int(input())
                print('Beli Buah yang lain?  : ')
                a = input()
                d += c
                x1 = c*kilo1
                x += x1
                if a == 'y' or a == 'Y':
                    continue
                if a == 'n'or a == 'N':
                    break
            if a == 'n'or a == 'N':
                break
            else:
                print('input tidak valid')
                exit()
        print('=======================================')
        print('Total Harga              :',x)
    except KeyError:
        print('Buah tidak tersedia atau input tidak valid')
    except ValueError:
        print('Masukkan bilangan bulat saja')
if b == 'c' or b == 'C':
    try:
        print('Data buah yang dihapus   : ',end=' ')
        f = input('')
        del data[f]
        print(data)
    except KeyError:
        print('Buah tidak ditemukan')

