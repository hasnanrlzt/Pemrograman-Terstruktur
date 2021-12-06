lokasi = open("c:/DataMahasiswa.txt", "r")
DataMahasiswa = {}
dataList = []
baca = lokasi.readlines()
List = list(baca)

for data in List:
    isi    = data.split('|')
    nim    = isi[0]
    nama   = isi[1]
    alamat = isi[2]
    alamat = alamat.replace('\n','')
    DataMahasiswa = {'NIM   ' : nim,
                     'Nama  ' : nama,
                     'Alamat' : alamat}
    dataList.append(DataMahasiswa)

print(dataList)
lokasi.close()

