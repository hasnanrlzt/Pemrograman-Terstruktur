import random
def shuffleString(x,n):
    Hasillist = []
    hasilList = []
    karakter = list(x)

    while True:
        random.shuffle(karakter)
        hasil = ''.join(karakter)
        a = hasil in Hasillist

        if a == False:
            Hasillist = Hasillist + [hasil]

        if len(Hasillist)== n :
            hasilList = Hasillist
            break

    return hasilList

print(shuffleString('aku',2))
print(shuffleString('aku',3))
print(shuffleString('aku',4))