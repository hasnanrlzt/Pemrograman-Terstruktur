i = 0
while (i < 10):
    print('Hello world')
    i +=1

print("=============================")
i = 2
while (i <= 20):
    print('Hello world')
    i += 2

print("=============================")
i = 0
while True:
    print('Hello world')
    i += 1
    if (i == 10):
        break

print("=============================")
# kotak bintang ajaib
kolom = 5
baris = 5

i = 0
while (i < baris):
    j = 0
    while (j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1

print("=============================")
# kotak bintang ajaib
kolom = 0
baris = 5

i = 0
while(i <= baris):
    j = 0
    while(j < kolom):
        print('* ', end='')
        j += 1
    print('')
    i += 1
    kolom += 1
print("=============================")
from random import randint
while True:
    bil = randint(0, 10)
    print(bil)
    if bil == 5:
        break

print("=============================")
from random import randint
sum = 0
while True:
    bil = randint(0,10)
    sum = sum + 1
    print(bil)
    if bil == 5:
        break
print('Jumlah perulangan : ' + str(sum))




































