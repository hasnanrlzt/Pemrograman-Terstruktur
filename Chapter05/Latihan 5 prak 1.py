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

tsia = A*0.1
tsib = B*0.1
tsic = C*0.1
tsid = D*0.1

taa = A*0.05
tab = B*0.05
tac = C*0.05
tad = D*0.05

gka = A + tsia + taa
gkb = B + tsia + tab
gkc = C + tsic + tac
gkd = D + tsid + tad

gba = gka - a
gbb = gkb - b
gbc = gkc - c
gbd = gkd - d

if (gk == "A"):
    print('Gaji pokok             : Rp',A )
    print('Tunjangan Istri/Suami  : Rp',tsia)
    print('Tunjangan anak         : Rp',taa)
    print('------------------------------------------')
    print('Gaji kotor             : Rp',gka)
    print('Potongan  (2.5%)       : Rp',a)
    print('Gaji Bersih            : Rp',gba)
if gk == "B":
    print('Gaji pokok             a : Rp',B)
    print('Tunjangan Istri/Suami   : Rp', tsib)
    print('Tunjangan anak          : Rp',tab)
    print('------------------------------------------')
    print('Gaji kotor              : Rp',gkb)
    print('Potongan (2.0%)         : Rp ', b)
    print('Gaji Bersih             : Rp',gbb)

if gk == "C":
    print('Gaji pokok             : Rp ',C)
    print('Tunjangan Istri/Suami  : Rp',tsic)
    print('Tunjangan anak         : Rp',tac)
    print('------------------------------------------')
    print('Gaji kotor             : Rp',gkc)
    print('Potongan (1.5%)        : Rp ', c)
    print('Gaji bersih            : Rp', gbc)
if gk == "D":
    print('Gaji pokok             : Rp',D)
    print('Tunjangan Istri/Suami  : Rp',tsid)
    print('Tunjangan anak         : Rp',tad)
    print('------------------------------------------')
    print('Gaji koto              : Rp',gkd)
    print('Potongan (1.5%)        : Rp ', d)
    print('Gaji bersih            : Rp', gbd)
else:
    print("Invalid!!! Golongan A/B/C/D")