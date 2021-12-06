note1 = print(' '*10, 'Petunjukk!!!',' '*10)
print('='*35)
note2= print('Masukkan nama dan alaamat file')
note3= print('Example: c:/dataASCII.txt')
print('='*35)
lokasi = str(input("Masukkan nama file: "))
asal = open(lokasi, 'r')
baca = asal.read()
mylist = list(baca)
List = []
nilaiN = int(input('Masukkan nilai n  : '))

for x in mylist:
    ascii = ord(x)
    if ascii == 32:
        ascii1 = ascii
    else:
        ascii1 = ascii + nilaiN
        if ascii1 > 122:
            ascii1 = ascii1 - 26
        elif ascii1 > 90 and ascii1 <97 :
            ascii1 = ascii1 - 26
    kode = chr(ascii1)
    List = List +[kode]
    if not mylist:
        break

gabungletter = ''.join(List)
tujuan = open('c:\\hasilASCII.txt', 'w')
tujuan.write(gabungletter)
asal.close()
tujuan.close()

