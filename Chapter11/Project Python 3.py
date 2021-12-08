from datetime import *

def diffDate(x):
    tanggal = datetime.date(datetime.now())
    year, month, day = x.split('-')
    searchtgl = date(int(year), int(month), int(day))
    selisih = tanggal - searchtgl
    selisihHari = abs(selisih.days)

    return selisihHari

lokasi = open('c:\Data Peminjam.txt', 'r')

print('=' * 50)
search = input('Masukkan Kode Member :')
print('=' * 50)

for x in lokasi:
    pecah = x.split('|')
    kode = pecah[0]
    nama = pecah[1]
    judul = pecah[2]
    mulai = pecah[3]
    maks = pecah[4]
    kembali = datetime.date(datetime.now())
    late = diffDate(pecah[4])
    denda = int(late) * 2000

    data = {'kode': kode,
            'nama': nama,
            'judul': judul,
            'mulai': mulai,
            'maks': maks,
            'kembali': kembali,
            'late': late,
            'denda': denda}

    if search == data['kode']:
        print('Data Peminjaman Buku \n')
        print('=' * 30)
        print('Kode Member              : ', data['kode'])
        print('Nama Member              : ', data['nama'])
        print('Judul Buku               : ', data['judul'])
        print('Tanggal Mulai Peminjaman : ', data['mulai'])
        print('Tanggal Maks Peminjaman  : ', data['maks'])
        print('Tanggal Pengembalian     : ', data['kembali'])
        print('Terlambat                : ', data['late'])
        print('Denda                    : ', data['denda'])

        lokasi.close()
        break

    if search != data['kode']:
        print('Data mahasiswa tidak ditemukan')
        lokasi.close()