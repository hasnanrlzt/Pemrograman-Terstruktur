def ubahHuruf(teks, a, b):
    rubah  = teks.replace(a, b)
    daftar = list(teks)
    hasil  = ' '.join([rubah])
    return hasil
print(ubahHuruf('MATEMATIKA','T','S'))

