lokasi =open('c:/DataMahasiswa.txt','r')
print('='*30)
search =input('Search NIM :')
print('='*30)

for x in lokasi:
    pecah  = x.split('|')
    nim    = pecah[0]
    nama   = pecah[1]
    alamat = pecah[2]
    data   ={'nim':nim,
             'nama':nama,
             'alamat':alamat}
    if search==data['nim']:
        print('Data Mahasiswa')
        print('='*30)
        print('NIM    : ', data['nim'])
        print('Nama   : ', data['nama'])
        print('Alamat : ', data['alamat'])
        lokasi.close()
        break

if search != data['nim']:
    print('Data mahasiswa tidak ditemukan')
    lokasi.close()

