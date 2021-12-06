lokasi = open("c:/DataMahasiswa.txt", "a")
while True:
    nim = input('Masukkan NIM: ')
    nama = input('Masukkan nama mahasiswa: ')
    alamat = input('Masukkan alamat ')
    susunan = nim+'|'+nama+'|'+alamat+'\n'
    lokasi.write(susunan)

    print('Ingin memilih lagi? (y/n) : ', end=' ')
    f = input()
    if f == 'Y' or f == 'y':
       continue

    if f == 'n' or f == 'N':
        break
    else:
        print('input tidak valid masukkan Y/N')
        print('Ingin memilih lagi? (y/n) : ', end=' ')
        f = input()
        if f == 'Y' or f == 'y':
            continue
        if f == 'n' or f == 'N':
            break
        else:
            print('input tidak valid ')
            break

lokasi.close()

