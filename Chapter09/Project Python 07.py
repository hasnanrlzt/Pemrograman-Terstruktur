print("===" * 22)
print('NIM'.ljust(10), 'NAMA MAHASISWA'.ljust(15),
      'TGL LAHIR'.center(21,' '), 'TEMPAT LAHIR'.center(15,' '), )
print("---" * 22)

data = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
for x in data:
    y = x.split(':')
    a = y[0]
    b = y[1]
    c = y[2]
    d = y[3]
    print(a.ljust(10), b.ljust(21),
          c.ljust(17), d.ljust(20))
print('---' * 22)

