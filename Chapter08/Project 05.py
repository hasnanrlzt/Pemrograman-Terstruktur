try:
    hasil = []
    bil = []
    def kuadrat ():
        global bil
        global hasil
        while True:
            bilangan = int(input('Bilangan yang ingin dimasukkan  : '))
            bil.append(bilangan)
            hasil.append(bilangan ** 2)
            tambah = str(input ('Ingin menambahkan lagi? (Y/N)  :'))
            if (tambah == 'y' or tambah == 'Y'):
                True
            elif (tambah == 'n' or tambah == 'N'):
                bil.sort()
                print('Daftar data bilangan  : ', bil)
                hasil.sort()
                print('Hasil kuadrat dari ', bil, '= ', hasil)
                break
            else:
                print('Maaf pilih Y/N !!!!!')
                tambah = str(input('Ingin menambahkan lagi? (Y/N)  :'))
    kuadrat()
except ValueError:
    print('Maaf data harus berupa anggka !!!!!')
bil.sort()
print('Daftar data bilangan  : ', bil)
hasil.sort()
print('Hasil kuadrat dari ', bil, '= ', hasil)


