def dataStat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    d = [a,b,c]
    return d
data = []

try:
    bil1 = int(input('Banyak bilangan yang diinginkan   : '))
except ValueError:
    print('Maaf input data didak valid !!!!!')
    bil1 = int(input('Banyak bilangan yang diinginkan   : '))
    x = 0
    print('==============================================')
    while (x < bil1):
        bil2 = int(input('Masukkan bilangan  : '))
        data.append(bil2)
        x += 1
        continue
except ValueError:
    print('Maaf input data tidak valid !!!!!')
try:
    x = 0
    while(x < bil1):
        bil2 = int(input('Masukkan bilangan  : '))
        data.append(bil2)
        x += 1
        continue
except ZeroDivisionError:
    print('Input harus berupa angka !!!!!')
except ValueError:
    print('Maaf input data tidak valid !!!!!')

print('==============================================')
hasil = dataStat(data)
print('Jadi, nilai rata-rata, nilai tertinggi, dan nilai terendah dari :', data,'adalah', hasil)


