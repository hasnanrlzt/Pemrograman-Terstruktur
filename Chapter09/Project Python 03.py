try:
    def bintang(n):
        a = n % 2
        b = n - a
        c = 1
        d = 1 + (a-1)*2
        e = 1 + a*2
        for i in range(b):
            x = "*" * c
            print(x.center(e))
            c += 2
        for i in range(a):
            y = "*" * d
            print(y.center(e))
            d -= 2
    n = int(input("Masukan banyak baris bintang : "))
    bintang(n)
except ValueError:
    print('Data harus interger')
