#diketahui BBM yang diperlukan 66.25l, kapasitas tangki 50l
import math
def Refill(jumlahbbm,kapasitas):
    return(jumlahbbm/kapasitas)

jumlahbbm= float(input("jumlah liter BBM yang diperlukan = "))
kapasitas= int(input('kapasitas liter tangki = '))
refill= Refill(jumlahbbm,kapasitas)
print('banyak tangki harus diisi = ', math.ceil(refill), "kali")