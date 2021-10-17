from random import randint
print('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!')
bil = randint(0,100)
scor = 100
while True:
    tebakan = int(input('Tebakan anda : '))
    if(tebakan > bil):
        print('Hehehe... Bilangan tebakan anda terlalu besar')
        scor -= 2
    elif(tebakan < bil):
        print('Hehehe... Bilangan tebakan anda terlalu kecil')
        scor -= 2
    elif(tebakan == bil):
        print('Ye ee.... Bilangan tebakan anda BENAR :-)')
        print('Scor Anda : ' + str(scor))
        break