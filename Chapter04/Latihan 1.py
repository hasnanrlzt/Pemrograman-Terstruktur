#waktu rental 06.00 - 23.50
#tarif 12 jam pertama Rp 200000 dan berikutnya 10000/jam
import math
print('====RENTAL MOBIL SUKA SUKA====')
def jam(jamrental,jamkembali):
    return jamkembali-jamrental
def menit(menitrental,menitkembali):
    return menitkembali-menitrental
def total(totaljam,totalmenit):
    return (totaljam*60)-totalmenit

#input data
print('waktu rental')
jamrental= int(input('jam ='))
menitrental= int(input('menit ='))
print('waktu mengembalikan')
jamkembali= int(input('jam ='))
menitkembali= int(input('menit ='))
totaljam= jam(jamrental,jamkembali)
totalmenit= menit(menitrental,menitkembali)
print('total rental =', totaljam, 'jam', totalmenit, 'menit')
rental= (totaljam + (totalmenit/60))
print('lama rental dalam jam', rental)
tarifawal = int(input('tagihan rental 12 jam ='))
tarifahir = int(input('tagihan rental lebih dari 12 jam ='))

if(rental > 12):
   print('total tagihan', (tarifawal) + (rental-12)*tarifahir)
elif(rental < 12):
    print('total tagihan =', tarifawal)
