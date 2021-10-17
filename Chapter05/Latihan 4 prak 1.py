print('Masukkan kode karyawan   :')
kk = str(input())
print('Masukkan nama karyawan   :')
nk = str(input())
print('Masukkan golongan        :')
gk = str(input())
print('=========================================')
print('STRUK RINCIAN GAJI KARYAWAN')
print('------------------------------------------')
print('Nama Karyawan     : ',nk,'( ',kk,' )')
print('Golongan          : ',gk)
print('------------------------------------------')

A = 10000000
B = 8500000
C = 7000000
D = 5500000

a = 0.025*A
b = 0.02*B
c = 0.015*C
d = 0.01*D

ab = A-a
bb = B-b
cb = C-c
db = D-d

if (gk == "A"):
    print('Gaji pokok     : Rp ',A )
    print('Potongan (2.5%): Rp ',a)
    print('------------------------------------------')
    print('Gaji bersih    : Rp',ab)
    if gk == "B":
        print('Gaji pokok     : Rp ',B)
        print('Potongan (2.0%): Rp ', b)
        print('------------------------------------------')
        print('Gaji bersih    : Rp', bb)
    if gk == "C":
        print('Gaji pokok     : Rp ',C)
        print('Potongan (1.5%): Rp ', c)
        print('------------------------------------------')
        print('Gaji bersih    : Rp', cb)
    if gk == "D":
        print('Gaji pokok     : Rp ',D)
        print('Potongan (1.5%): Rp ', d)
        print('------------------------------------------')
        print('Gaji bersih    : Rp', db)
else:
    print("Invalid!!! Golongan A/B/C/D")