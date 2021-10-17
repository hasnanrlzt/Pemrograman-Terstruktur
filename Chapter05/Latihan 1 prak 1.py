#syarat kelulusan: nilai > 60 & nilai matematika > 70
#nama = str(input "Nama   :")
#kelas = str(input "NIM    :")
print('Nilai Bahasa Indonesia :')
nilaibi = int(input())
print("Nilai IPA  :")
nilaiipa = int(input())
print('Nilai Matematika :')
nilaimtk = int(input())

if nilaibi >60 and nilaiipa >60 and nilaimtk >70:
    nilai = 'Lulus'
elif nilaibi <60 or nilaiipa <60 or nilaimtk <70:
    nilai = 'Tidak Lulus'

print('Status kelulusan = ' + nilai)



