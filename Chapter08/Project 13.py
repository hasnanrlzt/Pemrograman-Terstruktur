nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
def nilaiTinggi(nilaiMhs):
    x = 0
    y = {}
    for n in nilaiMhs:
        uas = n.get('uas')
        mid = n.get('mid')
        nilaiakhir = (mid + 2*uas)/3
        if(nilaiakhir>a):
            x = nilaiakhir
            y['nama'] = n.get('nama')
            y['nim'] = n.get('nim')
    print('Nilai tertinggi diraih oleh  ', b['nama'] ,'dengan NIM', b['nim'])
nilaiTinggi(nilaiMhs)

