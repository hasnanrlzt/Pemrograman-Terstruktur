# function sum(a,b,c,d,...)
def sum(*dataku):
    x = 0
    for x in dataku:
        x = x + y
    print('Jumlah seluruh nilai = ',x)

# function average(a,b,c,d,...)
def average(*dataku):
    x = 0
    jumlah = 0
    for y in dataku:
        jumlah = jumlah + 1
        x = (x + y) / jumlah
    print('Nilai rata rata = ',x)

# function maks(a,b,c,d,...)
def maks(*dataku):
    max = dataku[0]
    for nilai in dataku:
        if nilai > max:
            max = nilai
    print('Nilai maksimum = ', max)

# function min(a,b,c,d,...)
def min(*dataku):
    minimum = dataku[0]
    for bil in dataku:
        if bil < minimum:
            minimum = bil
    print('Nilai minimum = ',minimum)

