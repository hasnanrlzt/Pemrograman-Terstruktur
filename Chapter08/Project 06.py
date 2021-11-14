data = []
def sortStringByChar():
    while True:
        nama = str(input('Data yang ingin dimasukkan   : '))
        data.append(nama)
        yesNo = str(input('Ingin menambahkan lagi? (Y/N) '))
        if yesNo == 'y' or yesNo == 'Y':
            continue
        elif yesNo == 'y' or yesNo == 'N':
            print('List data :', data)
            data.sort(key = len, reverse = True)
            print('Urutan list dari jumlah karakter : ', data)
            break
        else:
            print('Input tidak valid !!!!!')
            yesNo = str(input('Ingin menambahkan lagi? (Y/N) '))
            if yesNo == 'y' or yesNo == 'Y':
                continue
            elif yesNo == 'y' or yesNo == 'N':
                print('List data :', data)
                data.sort(key=len, reverse=True)
                print('Urutan list dari jumlah karakter : ', data)
                break
sortStringByChar()


