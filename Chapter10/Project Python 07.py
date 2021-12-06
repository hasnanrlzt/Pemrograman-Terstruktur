lokasi = open('c:\hasilASCII.txt', 'r')
baca = lokasi.read()
data = list(baca)
mylist = []
nilaiN = int(input('Masukkan nilai n: '))

for soal in data:
    ascii = ord(soal)
    if ascii == 32:
        ascii1 = ascii
    else:
        ascii1 = ascii - nilaiN
        if ascii1 < 65:
            ascii1 = ascii1 + 26
        elif (90 < ascii1 and ascii1 <97):
            ascii1 = ascii1 + 26
    char = chr(ascii1)
    mylist.append(char)
gabungletter = ''.join(mylist)
tujuan = open('c:\ASCIIasli.txt', 'w')
tujuan.write(gabungletter)
lokasi.close()
tujuan.close()

