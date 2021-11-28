try:
    def bintang():
        x = 0
        z = 1
        while x < n:
            y = ('*'* z)
            z += 2
            x += 1
            print(y.center(10, ' '))
    n = int(input('Masukkan banyak baris yang diinginkan : '))
    bintang()
except ValueError:
    print('Data harus interger')
    n = int(input('Masukkan banyak baris yang diinginkan : '))
    bintang()

