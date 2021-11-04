# Masukkan data
# contoh file data c:/Try.txt
try:
    print('Masukkan nama file                   : ')
    inData = str(input())

    print('Data yang ingin ditambahkan          :')
    newdata = str(input())

    print('Mau lagi? (y/n)                      :')
    jawab = str(input())

    while jawab == 'y':
        print('Data yang ingin ditambahkan      :')
        newdata += str(input())
        print('Mau lagi? (y/n)                  :')
        jawab = str(input())
        if jawab == 'n':
            break

    f = open(inData, "a")
    f.write(newdata)
    f.close()

    f = open(inData, "r")
    print(f.read())
except FileNotFoundError:
    print('File tidak ditemukan')

