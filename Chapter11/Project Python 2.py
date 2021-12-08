from datetime import *
def DataPerpus():
    lokasi = open('c:\Data Peminjam.txt', 'w')
    tglPinjam = datetime.date(datetime.now())
    tglKembali = tglPinjam + timedelta(days=7)
    codeBK = input('Masukkan Kode Member   : ')
    nameBK = input('Masukkan Nama Member   : ')
    titleBK = input('Masukkan Judul Buku    : ')
    listData = [codeBK.upper(), nameBK, titleBK, str(tglPinjam), str(tglKembali)]
    hasil = '|'.join(listData) + '\n'
    lokasi.write(hasil)
    Qs = input('Ulangi lagi (y/n)      : ')

    while Qs == 'y' or Qs == 'Y':
        print('='*45)
        codeBK = input('Masukkan Kode Member   : ')
        nameBK = input('Masukkan Nama Member   : ')
        titleBK = input('Masukkan Judul Buku    : ')
        listData = [codeBK.upper(), nameBK, titleBK, str(tglPinjam), str(tglKembali)]
        hasil= '|'.join(listData) + '\n'
        lokasi.write(hasil)
        Qs = input('Ulangi lagi (y/n)      : ')
        if Qs == 'n'or Qs == 'N':
            break
    lokasi.close()
DataPerpus()
