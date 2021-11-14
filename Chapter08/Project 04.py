try:
    daftar = ['bayam', 'kangkung', 'wortel', 'selada']
    print('Daftar sayur :', daftar)
    print('PILIHAN :','\nA. Menambah data sayur','\nB. Menghapus data sayur','\nC. Menampilkan data sayur')
    while True:
        print('Pilihan (A/B/C) : ',end=' ')
        data = input()
        if data == 'A' or data == 'a':
            print('Tambahkan data sayur : ',end=' ')
            a = input()
            daftar.append(a)
        elif data == 'B' or data == 'b':
            print('Data sayur yang ingin dihapus : ', end=' ')
            b = input()
            if b in daftar:
                daftar.remove(b)
            else:
                print('Maaf data tidak ditemukan ')
        elif data == 'C' or data == 'c':
            c = set(daftar)
            d = list(c)
            print('Daftar data sayur : ',)
            for e in d:
                print(e)
        else:
            print('input tidak valid')
            continue
        print('Ingin memilih lagi? (y/n) : ', end=' ')
        f = input()
        if f == 'Y' or f == 'y':
            print('PILIHAN :', '\nA. Menambah data sayur', '\nB. Menghapus data sayur', '\nC. Menampilkan data sayur')
            continue
        if f == 'n' or f == 'N':
            break
        else:
            print('input tidak valid')
        continue
except ValueError:
    print('Maaf data tidak ditemukan ')

