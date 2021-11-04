# Contoh data (C:\myData.txt)
try:
    data = str(input('Masukkan nama file: '))
    file = open(data, 'r')
    print('isi file ', data, ' adalah :')
    print(file.read())
except FileNotFoundError:
    print('File tidak ditemukan')

