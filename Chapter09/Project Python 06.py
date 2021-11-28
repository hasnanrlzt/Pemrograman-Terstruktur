print("===" * 25)
print('NIM'.ljust(10), 'Nama'.ljust(15), 'N.MID'.ljust(10),
      'N.UAS'.ljust(10), 'N.AKHIR'.ljust(13), 'STATUS'.ljust(10))
print("---" * 25)

daftar = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
         {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
         {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]
for data in daftar:
    nilaiAkh = (data['mid'] + (2 * data['uas']))/3
    status   = 'LULUS'
    if(nilaiAkh < 60):
        status = 'TIDAK LULUS'
    print(data['nim'].ljust(10), data['nama'].ljust(15),
          str(data['mid']).rjust(5),str(data['uas']).rjust(10),
          str(round(nilaiAkh,2)).rjust(12), status.rjust(12))
print("---" * 25)
