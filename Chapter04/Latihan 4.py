import math
#ab: vr= 62 km/jam  s= 125 km
#bc: vr= 70 km/jam s= 256 km
# istirahat = 45 menit
# berangkat 06.00

s_ab = int(input('jarak dari kota a ke kota b = '))
vr_ab = int(input('kecepatan rata rata dari kota a ke b = '))
s_bc = int(input('jarak dari kota b ke kota c = '))
vr_bc = int(input('kecepatan rata rata dari kota b ke c = '))
istirahat = int(input('lama istirahat dalam menit = '))
jam_go = int(input("jam berangkat = "))
mnt_go = int(input("menit berangkat = "))

t_ab = (s_ab/vr_ab)*60 #120.96774193548387 menit
t_bc = (s_bc/vr_bc)*60 #219.42857142857142 menit
t_ac = t_ab + t_bc + istirahat # 385.3963133640553 menit
tot_jam = math.floor(t_ac/60)
tot_mnt = math.floor(t_ac % 60)

jam_sampe = tot_jam + jam_go
mnt_sampe = tot_mnt + mnt_go

#cek apakah jam sampai lebih dari pukul 24:00
if(jam_sampe > 24):
    jam_sampe = jam_sampe - 24
# print('jam_sampe = ', jam_sampe)

#cek apakah menit >= 60, apabila iya maka jam + 1
if(mnt_sampe >= 60):
    jam_sampe = jam_sampe + 1
    mnt_sampe = (mnt_go + tot_mnt) - 60


print('===========================================================')
print('total waktu ditempuh = ', tot_jam, 'jam', tot_mnt, 'menit')
print('sampai pada pukul = ', jam_sampe, ':', mnt_sampe)